import os
from tabpy.tabpy_server.app.app import app

# Expose "app" for gunicorn: start:app
# No need for app.run() when using gunicorn
