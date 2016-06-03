#-*- coding:utf-8 -*-

import MySQLdb

def mysql_con():
    global db, cursor
    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","","college")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

def mysql_clo():
    # 关闭数据库连接
    cursor.close()
    db.close()

def load_articles_all_type():
    type = ["bgxx", "bkjxjw", "xsgz", "kyyyjs", "dwhzjl"]
    typeName = {"bgxx":"办公信息", "bkjxjw":"本科教学教务", "xsgz":"学生工作", "kyyyjs":"科研与研究生", "dwhzjl":"对外合作交流"}
    articles_all_type = {}
    for t in type:
        articles_all_type[t] = load_articles(t)

    return articles_all_type,type,typeName

def load_articles(type):
    mysql_con()

    # 使用execute方法执行SQL语句
    sql = "SELECT * FROM article WHERE type='" + type + "' order by id;"
    cursor.execute(sql)

    # 获取数据库查询信息
    results = cursor.fetchall()

    mysql_clo()

    articles_one_type = []
    for row in results:
        id = row[0]
        title = row[1]
        content = row[2]
        author = row[3]
        type = row[4]
        article = {'id':id,'title':title,'content':content,'author':author,'type':type}
        articles_one_type.append(article)

    return articles_one_type

def show_article(id):
    mysql_con()

    sql = "SELECT * FROM article WHERE id = " + str(id)
    cursor.execute(sql)

    result = cursor.fetchone()

    mysql_clo()

    article = []
    id = result[0]
    title = result[1]
    content = result[2]
    author = result[3]
    type = result[4]
    article = {'id':id,'title':title,'content':content,'author':author,'type':type}

    return article




if __name__ == '__main__':
    print load_articles_all_type()
