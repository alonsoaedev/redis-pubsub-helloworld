# Redis Pub/Sub Hello World

## How to run

### First time

1. Create and run the container with Redis
``` bash
docker run -d --name redis-stack-server -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

2. Create the virtual environment to install Redis for python
``` bash
virtaulenv env
```

3. Activate the environment
``` bash
source env/bin/activate
```

4. Install redis for python
``` bash
pip install redis
```

5. Run the publisher script
``` bash
python publisher.py
```

6. Open another terminal

7. Activate the environment in the new terminal

8. Run the subscriber script
``` bash
python subscriber.py
```

### Development
1. Run the container with Redis
``` bash
docker run -d redis-stack-server -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

2. Activate the environment for publisher
``` bash
source env/bin/activate
```

5. Run the publisher script
``` bash
python publisher.py
```

6. Open another terminal

7. Activate the environment for subscriber

8. Run the subscriber script
``` bash
python subscriber.py
```

## Stop the project
1. Deactivate the environments
``` bash
deactivate
```

2. Stop the container with Redis
``` bash
docker stop redis-pubsub-server
```
