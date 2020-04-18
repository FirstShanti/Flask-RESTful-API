#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from view import users
from ETL_users import fetch_data

app.register_blueprint(users)

if __name__=="__main__":
	fetch_data(100)
	app.run(host='0.0.0.0', port=5000)