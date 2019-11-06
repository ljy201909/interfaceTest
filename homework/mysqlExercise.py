# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.06

import pymysql

#指定数据库地址、用户名、密码、端口号
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306)

#获取数据库游标
cursor = db.cursor()

#创建数据库
cursor.execute("CREATE DATABASE spiders DFFAULT CHARACTER AET utf8")

#创建数据表
sql1 = "CREATE TABLE IF NOT EXISTS students (id VERCHAR(255) NOT NULL,name VERCHAR(255) NOT NULL,age INT NOT NULL, PRIMARY KEY (id))"
cursor.execute(sql1)

#查询数据
sql2 = "select * from students where age>=20"
cursor.execute(sql2)
row = cursor.fetchone()
while row:
    print('Row：',row)
    row = cursor.fetchone()

db.close()