#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

import requests

# 请求发送到百度，并获取源码
response = requests.get("http://www.baidu.com")
# 指定编码为 utf-8
response.encoding = 'UTF-8'
print(response.text)
print('-------------------')
print(response.status_code)
print('-------------------')
print(requests.head("http://www.baidu.com").headers)
print('-------------------')
# 根据URL抓取图片并保存
response = requests.get('https://pic3.zhimg.com/50/v2-06ac19750e235cfe8b97600c5c3700a1_400x224.png')
print(response.content)

with open('/Users/sage/Pictures/test.jpg', 'wb') as f:
	f.write(response.content)
	print(f.close())
