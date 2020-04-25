#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from view import users
from fill_db import fill_db

app.register_blueprint(users)

if __name__=="__main__":
	fill_db()
	app.run(host='0.0.0.0', port=5000)