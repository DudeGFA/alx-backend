var kue = require('kue')
 , queue = kue.createQueue();

queue.process('push_notification_code', function(job, done){
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}
