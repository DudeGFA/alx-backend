var kue = require('kue')
queue = kue.createQueue();

job_data = {
    'phoneNumber': '08088674775',
    'message': 'Tersting the connection',
  }

const job = queue.create('push_notification_code', job_data).save( function(err){
   if( !err ) console.log( `Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed')
}).on('failed', () => {
    console.log('Notification job failed')
})
