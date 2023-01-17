import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from sendCircuit import sendCircuit

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

from app import routes