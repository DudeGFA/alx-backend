var kue = require('kue')
 , queue = kue.createQueue();

queue.process('push_notification_code', function(job, done){
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacklist.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}