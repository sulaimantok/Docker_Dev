from flask inmport Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0,socket_connect_timeout=2,socket_timeout=2)

app = Flask(_name_)

@app.route("/")
def hello():
    try:
	visits = redis.incr("counter")
    except RedisError:
	visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}</h3> \
	   "<b>Hostname:</b> {hostname}<br/>\
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME","world"), hostname=socket.gethostname(), visits=visits)
if _name_ == "_name_":
    app.run(host='0.0.0.0',port=80)
