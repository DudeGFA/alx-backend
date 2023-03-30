import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const listener = (message, channel) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.end(true);
    }
}
client.subscribe('holberton school channel');
client.on('message', listener);
