import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue();

jobs.forEach((job_Data) => {
  const createJob = queue.create('push_notification_code_2', job_Data)
    .save((error) => {
      if (error) {
        console.log(`Notification job ${createJob.id} failed: ${error}`);
      }
      console.log(`Notification job created: ${createJob.id}`);
    });

  createJob.on('complete', () => {
    console.log(`Notification job ${createJob.id} completed`);
  }).on('failed', (errMsg) => {
    console.log(`Notification job ${createJob.id} failed: ${errMsg}`);
  }).on('progress', (progress) => {
    console.log(`Notification job ${createJob.id} ${progress}% complete`);
  });
});
