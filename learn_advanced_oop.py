#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
from types import MethodType


class Student(object):
	def __index__(self):
		pass


def set_name(self, name):
	self.name = name


def get_name(self):
	return self.name


if __name__ == '__main__':
	s = Student()
	# 为实例绑定属性
	s.name = 'sage'
	print('name is ', s.name)

	# 为实例绑定方法
	s.set_name = MethodType(set_name, s)
	s.get_name = MethodType(get_name, s)
	s.set_name('guo')
	print('the name got is', s.get_name())
