bind = "0.0.0.0:80"
workers = 1
backlog = 2048
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
timeout = 600
debug = False