#!/usr/bin/env python3
import sys
sys.path.insert(0, "/var/www/catalog/")
from app import app as application
# based on http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/