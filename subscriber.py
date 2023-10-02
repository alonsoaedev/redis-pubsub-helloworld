import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# pubsub() method creates the pubsub object
pubsub = r.pubsub()

# use .subscribe() method to subscribe to topic on which you want to listen for messages
pubsub.subscribe("get_states")

# .listen() returns a generator over which you can iterate and listen for messages from publisher
for message in pubsub.listen():
    if message['type'] == 'subscribe':
        print(f'Listeninig to channel {message["channel"]}...')
        continue

    print(message['data']) # <-- you can literally do any thing with this message i am just printing it