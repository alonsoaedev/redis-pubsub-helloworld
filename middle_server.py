import redis
import json

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# pubsub() method creates the pubsub object
pubsub = r.pubsub()

channels = [
    'add_state',
    'change_status',
]

def add_state(json_raw: str):
    state = json.loads(json_raw)
    r.lpush('state_ids', state['id'])
    r.hset(
        f'states:{state["id"]}', 
        mapping={
            'id': state['id'],
            'status': state['status']
        }
    )

def change_status(json_raw: str):
    state = json.loads(json_raw)
    r.hset(f'states:{state["id"]}', 'status', state['status'])

def get_states():
    ids = r.lrange('state_ids', 0, -1)
    states = []
    for id in ids:
        state = r.hgetall(f'states:{id}')
        states.append(state)
    return states

# use .subscribe() method to subscribe to topic on which you want to listen for messages
for channel in channels:
    pubsub.subscribe(channel)

# .listen() returns a generator over which you can iterate and listen for messages from publisher
for message in pubsub.listen():
    if message['type'] == 'subscribe':
        print(f'Listeninig to channel {message["channel"]}...')
        continue

    if message['channel'] == 'get_states':
        print(message['data'])
        continue

    if message['channel'] == 'add_state':
        add_state(message['data'])

    if message['channel'] == 'change_status':
        change_status(message['data'])

    r.publish('get_states', json.dumps(get_states(), indent = 4))
    print('Publishing to chanel get_states...')