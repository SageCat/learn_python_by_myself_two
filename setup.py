#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

import requests
from selenium import webdriver

# 请求发送到百度，并获取源码
response = requests.get("http://www.baidu.com")
# 指定编码为 utf-8
response.encoding = 'UTF-8'
print(response.text)
print(response.status_code)
# 根据URL抓取图片并保存
response = requests.get('https://pic3.zhimg.com/50/v2-06ac19750e235cfe8b97600c5c3700a1_400x224.png')
print(response.content)

with open('/Users/sage/Pictures/test.jpg', 'wb') as f:
	f.write(response.content)
	print(f.close())

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.page_source)

