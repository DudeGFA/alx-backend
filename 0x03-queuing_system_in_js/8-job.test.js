import { describe, it, before, after, afterEach } from "mocha";
import { expect } from 'chai';
import { createQueue } from "kue";

import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('createPushNotificationsJobs', function() {
    before(() => {
        queue.testMode.enter();
    })
    afterEach(() => {
        queue.testMode.clear();
    })
    after(() => {
        queue.testMode.exit();
    })

    it('throws error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('Test whether jobs are created', function() {
        const jobs = [
            {
                phoneNumber: '4159518782',
                message: 'This is the code 4321 to verify your account'
            },
            {
                phoneNumber: '4158718781',
                message: 'This is the code 4562 to verify your account'
            },
        ];

        createPushNotificationsJobs(jobs, queue);
    
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
    })
})
