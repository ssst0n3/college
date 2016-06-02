#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template
from app import app

# 首页
@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World! This is a index page! But our designer have not give me the index page! <br> <a href="xxgg">信息公告</a> &emsp; <a href="xygk">学院概况</a> &emsp; <a href="admin">后台管理</a>'

# 信息公告页
@app.route('/xxgg/')
def xxgg():
    pagename = "信息公告"
    return render_template("xinxigonggao.html", pagename = pagename)

# 学院概况页
@app.route('/xygk/')
def xygk():
    pagename = "学院概况"
    return render_template("xueyuangaikuang.html", pagename = pagename)

# 文章模板
@app.route('/article/')
@app.route('/article/<int:id>')
def article(id=None):
    # 数据库操作，返回title， content等信息
    if id:
        title = "我是一篇id为" + str(id) + "的文章的标题"
        content = "我是一篇id为" + str(id) + "的文章的内容"
        return render_template('article.html', title=title, content=content)
    else:
        return 'illegal access'

# 后台管理路由
@app.route('/admin/')
def admin():
    return '后台管理界面'

# 检索功能由第三方提供
# 评论、分享功能由多说提供
