"""Gunicorn configuration file."""

from os import environ, path

from dotenv import load_dotenv

# Read environment variables from ".env" file.
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Fetch deployment environment from environment variables.
ENVIRONMENT = environ.get("ENVIRONMENT")

proc_name = "broiestbot-db"
wsgi_app = "wsgi:app"
bind = "unix:broiestbot-db.sock"
threads = 4
workers = 2

if ENVIRONMENT == "development" or ENVIRONMENT is None:
    reload = True
    workers = 1
    threads = 1
    bind = ["127.0.0.1:8000"]
elif ENVIRONMENT == "production":
    access_log_format = "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
    daemon = True
    accesslog = "/var/log/broiestbot-db/info.json"
    errorlog = "/var/log/broiestbot-db/error.json"
    loglevel = "trace"
    dogstatsd_tags = "env:production,service:broiestbot-db,language:python"
else:
    raise ValueError(f"Unknown environment provided: `{ENVIRONMENT}`. Must be `development` or `production`.")
