import redis

# initializing the redis instance
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True # <-- this will ensure that binary data is decoded
)

options = [
    'exit',
    'add_state',
    'change_status',
]

def show_options(options: list):
    for index, option in enumerate(options):
        print(f'{index}) {option}')

show_options(options)
option = int(input('Option: '))
while option != 0:
    message = input(f'{options[option]}: ')
    r.publish(options[option], message)
    show_options(options)
    option = int(input('Option: '))
