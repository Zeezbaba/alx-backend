import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    kue.Job.testMode.enter();
  });

  afterEach(() => {
    kue.Job.testMode.exit();
    queue.testMode.clear();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('job is not an array');
  });

  it('should create jobs for each element in the jobs array', () => {
    const jobs = [
      { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account'},
      { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account'}
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[1]);
  });

  it('log appropriate response for jobs created, in-progress, completed or failed', () => {
    const jobs = [
      { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account'}
    ];

    const spyConsle = {
      log: [],
      info: console.log,
      logHandler: (message) => {
        spyConsle.log.push(message);
        spyConsle.info(message);
      }
    };

    console.log = spyConsle.logHandler;

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].on('complete', () => {
      expect(spyConsle.log).to.include(`Notification job ${queue.testMode.jobs[0].id} completed`);
      done();
    });
    queue.testMode.jobs[0].emit('complete');
  });
});
