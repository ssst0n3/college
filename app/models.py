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

# 查询数据表名
# 数据表变化少，可以固定下来
def get_tableName():
    mysql_con()
    sql_tableName = "SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = 'college';"
    cursor.execute(sql_tableName)
    results = cursor.fetchall()
    mysql_clo()
    tableNames = []
    for row in results:
        tableNames.append(row[0])
    return tableNames

# 查询数据字段名
# 数据字段名变化少，可以固定下来
def get_columns_of_table():
    columns_all_tables = {}
    mysql_con()
    for tableName in tableNames_init:
        sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE table_name = '" + tableName + "' AND table_schema = 'college';"
        cursor.execute(sql)
        results = cursor.fetchall()
        columns = []
        for row in results:
            columns.append(row[0])
        columns_all_tables[tableName] = columns
    mysql_clo()
    return columns_all_tables

# update更新数据库
def update_table_by_id(tableName, column, edit_data, id):
    if column != 'id':
        mysql_con()
        sql = "UPDATE " + tableName + " SET " + column + "='" + edit_data + "' WHERE id=" + id + ";"
        print sql
        cursor.execute(sql)

        db.commit()
        mysql_clo()
        initData()
        return 'success'
    else:
        return 'id cannot be changed'

# 按照id查询文章
def load_article_by_id(id):
    mysql_con()

    sql = "SELECT * FROM articles WHERE id = " + str(id)
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

# 按照id为序查找所有数据
def load_table_order_by_id(tableName):
    mysql_con()

    sql = "SELECT * FROM " + tableName + " order by id;"
    cursor.execute(sql)

    results = cursor.fetchall()

    mysql_clo()

    data_all_order_by_id = []
    for row in results:
        columns = columns_all_tables_init[tableName]
        data = {}
        for i in range(len(columns)):
            data[columns[i]]=row[i]
        data_all_order_by_id.append(data)
    return data_all_order_by_id

# 为bgxx服务
# 按照文章类型分类
def load_articles_classfied_by_type():
    type = ["bgxx", "bkjxjw", "xsgz", "kyyyjs", "dwhzjl"]
    typeName = {"bgxx":"办公信息", "bkjxjw":"本科教学教务", "xsgz":"学生工作", "kyyyjs":"科研与研究生", "dwhzjl":"对外合作交流"}
    articles_all_type = {}
    for t in type:
        articles_all_type[t] = load_table_by_column_order_by_id("articles","type",t)

    return articles_all_type,type,typeName

# 按照字段名查询一类信息
def load_table_by_column_order_by_id(tableName, column, column_data):
    mysql_con()

    # 使用execute方法执行SQL语句
    sql = "SELECT * FROM " + tableName + " WHERE " + column + "='" + column_data + "' order by id;"
    cursor.execute(sql)

    # 获取数据库查询信息
    results = cursor.fetchall()

    mysql_clo()

    data_all_one_column = []
    for row in results:
        columns = columns_all_tables_init[tableName]
        data = {}
        for i in range(len(columns)):
            data[columns[i]]=row[i]
        data_all_one_column.append(data)
    return data_all_one_column




def init_load_articles_classfied_by_type():
    return load_articles_classfied_by_type_init

def init_load_table_order_by_id_users():
    return load_table_order_by_id_users_init, columns_all_tables_init["users"]

def init_load_table_order_by_id_articles():
    return load_table_order_by_id_articles_init, columns_all_tables_init["articles"]

def initData():
    global tableNames_init, columns_all_tables_init, load_articles_classfied_by_type_init, load_table_order_by_id_users_init,load_table_order_by_id_articles_init
    tableNames_init = get_tableName()
    columns_all_tables_init = get_columns_of_table()
    load_articles_classfied_by_type_init = load_articles_classfied_by_type()
    load_table_order_by_id_articles_init = load_table_order_by_id("articles")
    load_table_order_by_id_users_init = load_table_order_by_id("users")

initData()

if __name__ == "__main__":
    print init_load_table_order_by_id_users()
