# flask-redis-rest

### How to run (1)
1. install docker and docker-compose
2. clone this repo
3. change directory to cloned repo
4. run in terminal - `docker-compose up --build`

you should see --

```
flask-redis-rest |  * Serving Flask app "app" (lazy loading)
flask-redis-rest |  * Environment: production
flask-redis-rest |    WARNING: This is a development server. Do not use it in a production deployment.
flask-redis-rest |    Use a production WSGI server instead.
flask-redis-rest |  * Debug mode: on
flask-redis-rest |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
flask-redis-rest |  * Restarting with stat
flask-redis-rest |  * Debugger is active!
flask-redis-rest |  * Debugger PIN: 954-304-063
```

### How to run (2) (Optional)
1. You need to have install redis-server from here https://redis.io/download
2. clone this repo
3. change directory to cloned repo
4. make virtual environment from python 3.6 and activate it
5. run in terminal - `pip install -r requirements.txt`
6. run in terminal - `python -m flask run`

you should see --

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
