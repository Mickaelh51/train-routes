#!/usr/bin/env python
from flask_apps import *

if __name__ == '__main__':
    app.run(host=app.config['LISTENIP'], port=app.config['LISTENPORT'], debug=app.config['DEBUG'])
