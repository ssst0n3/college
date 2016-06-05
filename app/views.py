#-*- coding:utf-8 -*-

import sys
# import json
from models import *

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
    articles,type,typeName = init_articles_xxgg()
    # articles_json = json.dumps(articles)
    # return render_template("xinxigonggao.html", pagename = pagename, articles=articles_json)
    return render_template("xinxigonggao.html", pagename = pagename, articles=articles, type = type, typeName = typeName)

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
    article_info = load_article_by_id(id)

    if id:
        title = article_info['title']
        content = article_info['content']
        return render_template('article.html', title=title, content=content)
    else:
        return 'illegal access'

# 后台管理路由
@app.route('/admin/')
@app.route('/admin/<string:operation>/')
@app.route('/admin/<string:operation>/<string:tableName>')
def admin(operation=None, tableName=None):
    if operation:
        if operation == 'show_tables':
            if tableName:
                exec ("records, columns = init_" + tableName + "_admin()")
                return render_template("admin_templates/tables-data.html", tableName = tableName, records = records, columns = columns)
            else:
                return render_template("admin_templates/tables-data.html")
        else:
            return 'index'
    else:
        return 'index'

# 检索功能由第三方提供
# 评论、分享功能由多说提供
