import kue from 'kue';

const queue = kue.createQueue();

const job_data = {
  phoneNumber: '9032859793',
  message: 'hello, I am Zeezbaba',
}

const createJob = queue.create('push_notification_code', job_data)
  .save((error) => {
    if (error) {
        console.error('Notification job failed', error);
    }
    console.log(`Notification job created: ${createJob.id}`);
  });

  createJob.on('complete', () => {
    console.log('Notification job completed');
  }).on('failed', () => {
    console.log('Notification job failed');
  });
