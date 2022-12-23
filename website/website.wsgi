#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/data/Pawsey_SpinQ/website/")

from app import app as application
application.secret_key = "hello"