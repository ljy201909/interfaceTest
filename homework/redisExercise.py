# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.09

from redis import StrictRedis

#连接Redis
redis = StrictRedis(host='localhost',port=6379,db= 0,password=None)
#创建键值对
redis.set('name','Bob')
#打印name键的值
print(redis.get('name'))


