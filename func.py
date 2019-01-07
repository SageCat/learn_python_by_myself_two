#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo


# return None
def hello_func():
	print('hello func')


def return_hello_func():
	return 'hello sage'


def para_hello_func(greeting, name='You', age=20):
	return '{}, {}, you are {} years old'.format(greeting, name, age)


# * 号隔开位置参数和命名关键字参数，或者使用可变参数隔开也能达到同样的效果
# 命名关键字参数，在调用函数时不可省略，但是如果命名关键字参数具有缺省值，调用时可以省略
def person(name, age, *, address, job):
	print('name', name)
	print('age', age)
	print('address', address)
	print('job', job)
	print('>>>>>>>>>>>>')


def person_two(name, age, *others, city, district):
	print(name, age, others, city, district)
	print('>>>>>>>>>>>>>>>>>>>>>>>')


# * represents tuple, 可变参数必须指向不变对象。
# ** represents dictionary
def student_info(*args, **kwargs):
	print(type(args))  # tuple
	print(args)
	print(type(kwargs))  # dictionary
	print(kwargs)


def mix(name, age=24, *value, city, **other):
	print('name', name)
	print('age ', age)
	for i in value:
		print(i)
	print('city', city)
	print(other)
	print('-----------------------')


hello_func()
print(return_hello_func())
print(para_hello_func('Hello', 'sage', 24))
print(para_hello_func('Hi', name='sage2', age=40))
student_info([1, 2, 3], name='sage', age=23)
course = ('Math', 'English', 'Chinese')
info = {'sage': 23, 'Ali': 24}
student_info(*course, **info)
student_info(*course, city='sage', age=23, address='futian')
print('----------------')
# 创建字典并打印
print(dict(a=12, b=34, c='sage'))
person('sage', 23, address='beijing', job='engineer')
person('sage', 23, address='Shanghai', job='software engineer')
person_two('sage', 40, 'high school', 1994, 6, 26, city='ShenZhen', district='LongGang')
mix('sage', 24, ('math', 'english', 'history'), nation='China', job='engineer', city='ShenZhen')
mix(*course, **info, city='SZ')

L = (x * x for x in range(10))
for i in L:
	print(i)

iter_course = iter(course)
print(next(iter_course))
print(next(iter_course))
print('--------')
for i in iter_course:
	print(i)
