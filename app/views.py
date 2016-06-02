#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/xxgg/')
def xxgg():
    pagename = "信息公告"
    return render_template("xinxigonggao.html", pagename = pagename)

@app.route('/xygk/')
def xygk():
    pagename = "学院概况"
    return render_template("xueyuangaikuang.html", pagename = pagename)
