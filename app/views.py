#-*- coding:utf-8 -*-

import sys
from flask import json, request
from models import *

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template
from app import app

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


# 信息公告页
@app.route('/xxgg/')
def xxgg():
    pagename = "信息公告"
    articles,type,typeName = load_articles_classfied_by_type()
    # articles_json = json.dumps(articles)
    # return render_template("xinxigonggao.html", pagename = pagename, articles=articles_json)
    return render_template("xinxigonggao.html", pagename = pagename, articles=articles, type = type, typeName = typeName)




@app.route('/teacher/')
@app.route('/teacher/<int:id>')
def teacher(id=None):
    if id == 1:
        return render_template("caoshujin.html")
    else:
        return render_template("teacher.html")



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
    article_info = load_table_by_id("articles", id)

    if id:
        title = article_info['title']
        content = article_info['content']
        return render_template('article.html', title=title, content=content)
    else:
        return 'illegal access'

# 后台管理路由
@app.route('/admin/')
@app.route('/admin/<string:operation>/', methods=['GET','POST'])
@app.route('/admin/<string:operation>/<string:tableName>', methods=['GET','POST'])
def admin(operation=None, tableName=None, action="show"):
    if operation:
        if operation == 'show_tables':
            if tableName == 'users' or tableName == 'articles':
                exec ("records, columns = init_load_table_order_by_id_" + tableName + "()")
                return render_template("admin_templates/tables-data.html", tableName = tableName, records = records, columns = columns).encode("utf-8")
            else:
                return render_template("admin_templates/tables-data.html")
        elif operation == 'load_data':
            exec ("records, columns = init_load_table_order_by_id_" + tableName + "()")
            for i in range(len(records)):
                records[i]["DT_RowId"]="row_"+str(records[i]["id"])
            return json.dumps({"data":records})
        elif operation == 'edit_table':
            data_submitted = dict(request.form)
            action = data_submitted['action'][0]
            del data_submitted['action']
            rows = []
            data_recieve = {}
            for k,d in data_submitted.items():
                DT_RowId = k[k.find('[')+1:k.find(']')]
                key = k[k.find(']')+2:-1]
                data = "".join(d)
                if DT_RowId not in rows:
                    rows.append(DT_RowId)
                    if action != 'create':
                        exec("data_recieve['" + DT_RowId + "'] = " + str(load_table_by_id(tableName, DT_RowId[4:])))
                        exec("data_recieve['" + DT_RowId + "']['DT_RowId'] = '" + DT_RowId + "'")
                    else:
                        exec("data_recieve['" + DT_RowId + "'] = {}")
                exec("data_recieve['" + DT_RowId + "']['" + key + "'] = '" + data + "'")

            data_response = []
            if action == 'edit':
                for k,d in data_recieve.items():
                    data_response.append(d)
                    edit_data = ""
                    for k2,d2 in d.items():
                        if k2 != 'id' and k2 != 'DT_RowId':
                            edit_data = edit_data + k2 + '=' + "'" + d2 + "',"
                    edit_data = edit_data[:-1]
                    print update_table_by_id(tableName, edit_data, k[4:])
            elif action == 'remove':
                for DT_RowId in rows:
                    delete_table_by_id(tableName, DT_RowId[4:])
            elif action == 'create':
                columns = ""
                values = ""
                for k,d in data_recieve['0'].items():
                    columns = columns + k + ','
                    values = values + d + ','
                edit_data = "(" + columns[:-1] + ") VALUES (" + values[:-1] + ")"
                insert_table(tableName, edit_data)
                # print data_recieve
                data_response.append(data_recieve['0'])

            return json.dumps({"data":data_response})
        else:
            return 'index'
    else:
        return 'index'

# 检索功能由第三方提供
# 评论、分享功能由多说提供





@app.route('/test')
def test():
    return render_template("st0n3.html")
