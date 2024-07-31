import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// creating a redis client
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync('available_seats');
  return availableSeats;
}

reserveSeat(50);
let reservationEnabled = true;

const queue = kue.createQueue();

const app = express();
const PORT = 1245;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ "status": "Reservation are blocked" });
  }

  const job = queue.create('reserve_seat').save((error) => {
    if (error) {
      return res.json({ "status": "Reservation failed" });
    }
    return res.json({ "status": "Reservation in process" });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err_msg) => {
    console.log(`Seat reservation job ${job.id} failed: ${err_msg}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ "status": "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    const seatsAvailable = await getCurrentAvailableSeats();
    if (seatsAvailable <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    const seatsA = seatsAvailable - 1;
    await reserveSeat(seatsA);

    if (seatsA === 0) {
      reservationEnabled = false;
    }
    done();
  });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
