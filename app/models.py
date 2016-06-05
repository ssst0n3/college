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


# 为信息公告服务，提供按照类型分类的文章
def init_articles_xxgg():
    global type_init, typeName_init, articles_classfied_by_type_init
    return type_init, typeName_init, articles_classfied_by_type_init

# 为后台管理服务，提供按照日期排序的文章
def init_articles_admin():
    global articles_admin_init, articles_admin_columns
    articles_admin_columns = ['id','title','content','author','type']
    return articles_admin_init, articles_admin_columns

# 为后台管理服务, 提供按照日期排序的文章
def init_users_admin():
    global users_admin_init, users_admin_columns
    users_admin_columns = ['id','username','email','role']
    return users_admin_init, users_admin_columns






# 按照文章类型分类
def load_articles_classfied_by_type():
    type = ["bgxx", "bkjxjw", "xsgz", "kyyyjs", "dwhzjl"]
    typeName = {"bgxx":"办公信息", "bkjxjw":"本科教学教务", "xsgz":"学生工作", "kyyyjs":"科研与研究生", "dwhzjl":"对外合作交流"}
    articles_all_type = {}
    for t in type:
        articles_all_type[t] = load_articles_by_type(t)

    return articles_all_type,type,typeName

# 按照类型查询文章
def load_articles_by_type(type):
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

# 按照时间为序查询文章
def load_articles_order_by_date():
    mysql_con()

    sql = "SELECT * FROM article"
    cursor.execute(sql)

    results = cursor.fetchall()

    mysql_clo()

    articles = []
    for row in results:
        id = row[0]
        title = row[1]
        content = row[2]
        author = row[3]
        type = row[4]
        article = {'id':id,'title':title,'content':content,'author':author,'type':type}
        articles.append(article)

    return articles


# 按照id查询文章
def load_article_by_id(id):
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

# 按照id为序查找所有user
def load_users_order_by_id():
    mysql_con()

    sql = "SELECT * FROM users order by id;"
    cursor.execute(sql)

    results = cursor.fetchall()

    mysql_clo()

    users = []
    for row in results:
        id = row[0]
        username = row[1]
        email = row[3]
        role = row[4]
        user = {"id":id, "username":username, "email":email, "role":role}
        users.append(user)

    return users

type_init, typeName_init, articles_classfied_by_type_init = load_articles_classfied_by_type()
articles_admin_init = load_articles_order_by_date()
users_admin_init = load_users_order_by_id()


if __name__ == '__main__':
    print load_articles_all_type()
