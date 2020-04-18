#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from view import users


app.register_blueprint(users)


if __name__=="__main__":
	app.run(port=5000)