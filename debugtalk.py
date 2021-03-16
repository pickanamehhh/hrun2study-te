#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: debugtalk.py
# @time: 2020/11/4 8:30 下午
import os
import random
import requests
from faker import Faker
import pymysql
#设置代理
# os.environ['http_proxy'] = 'http://127.0.0.1:8888'
# os.environ['https_proxy'] = 'https://127.0.0.1:8888'

def get_search_word():
    word_list = ['newdream','12306','火车票','新梦想软测教育']
    num = random.randint(0,len(word_list)-1)
    return word_list[num]

def s():
    print( '测试用例开始执行' )
def t():
    print('测试用例结束执行')

def s1(step_name):
    print( '测试步骤 [%s] 开始执行'%step_name )
def t1(step_name):
    print('测试步骤 [%s] 结束执行'%step_name)

def get_true():
    return None

def get_access_token():
    p_dict = {
        'grant_type': 'client_credential',
        'appid': 'wx55614004f367f8',
        'secret': '65515b46dd758dfdb09420bb7db2c67f'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=p_dict)
        token = response.json()['access_token']
    except KeyError as e:
        token = None
    return token
# 参数实战：
def get_params01():
    return ['newdream','12306','火车票']
def get_params02():
    return [['newdream','newdream_百度搜索'],['12306','12306_百度搜索'],['火车票','火车票_百度搜索']]
def get_random_int(min,max,count=3):
    num_list = []
    for i in range(count):
        num_list.append( random.randint(min,max) )
    return num_list

def get_random_string(base_str,str_len,count=3):
    base_str = base_str + '!@#¥%^'
    string_list = []
    for i in range(count):
        string = ''
        for j in range(int(str_len)):
            string = string + base_str[random.randint(0,len(base_str)-1)]
        string_list.append(string)
    return string_list

def get_random_phonenum(*mobile_num,count=3):
    phonenum_list = []
    for i in range(count):
        phone_start = str(random.choice(mobile_num))
        phone_end = ''.join( random.sample('0123456789',8) )
        phonenum_list.append( phone_start + phone_end )
    return phonenum_list

def get_random_name(count=3):
    f = Faker(locale='zh_CN')
    name_list = []
    for i in range(count):
        name_list.append( f.name() )
    return name_list

def get_params_by_mysql(case_name):
    mysql_connect = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    database='api_test', charset='utf8')
    cur = mysql_connect.cursor()
    cur.execute("select test_data,excepted_result from test_data where case_name like '%s%%';"%case_name)
    case_data = cur.fetchall()
    cur.close()
    mysql_connect.close()
    list_case_data = list(case_data)
    for i in range(len(list_case_data)):
        list_case_data[i] = list(list_case_data[i])
    return list_case_data

def to_ISO_8859_1(str):
    return str.encode('utf8').decode('iso8859-1')
def to_UTF_8(str):
    return str.encode('iso8859-1').decode('utf8')

if __name__=='__main__':
    print( get_params_by_mysql('test_baidu_search')  )
    # mysql_connect = pymysql.connect(host='localhost',port=3306,
    #                                 user='root',password='123456',
    #                                 database='api_test',charset='utf8')
    # # cur = mysql_connect.cursor(cursor=pymysql.cursors.DictCursor) #默认元组类型数据 ，返回字典类型
    # cur = mysql_connect.cursor() #默认元组类型数据 ，返回字典类型
    # cur.execute("select test_data,excepted_result from test_data where case_name like '%s%%';"%'test_baidu_search')
    # # print( cur.fetchone() )
    # print( cur.fetchall() )
    # cur.close()
    # mysql_connect.close()

