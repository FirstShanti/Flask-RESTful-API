#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from view import users

app.register_blueprint(users, url_prefix='/')

if __name__=='__main__':
	app.run(host='0.0.0.0', port=5001)