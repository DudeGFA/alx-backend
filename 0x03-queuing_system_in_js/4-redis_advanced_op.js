import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.hset('HolbertonSchools', 'Portland', 50, print)
client.hset('HolbertonSchools', 'Seattle', 80, print)
client.hset('HolbertonSchools', 'New York', 20, print)
client.hset('HolbertonSchools', 'Bogota', 20, print)
client.hset('HolbertonSchools', 'call', 40, print)
client.hset('HolbertonSchools', 'Paris', 2, print)

client.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
        console.log(error);
        throw error;
    }
    console.log(result);
});