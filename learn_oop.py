#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo


class Student(object):
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address

	def get_info(self):
		print('info of Student is name: %s, age: %s, address: %s' % (self.name, self.age, self.address))

	def get_age_level(self):
		if self.age < 0:
			return 'illegal age'
		elif 10 > self.age > 0:
			return 'Child'
		else:
			return 'Teenager'


if __name__ == '__main__':
	student = Student('sage', 24, 'HeBei')
	student.get_info()
	print(student.get_age_level())
	print(type(type))
