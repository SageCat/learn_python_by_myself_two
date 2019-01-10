#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
import types


class Student(object):
	# 类变量
	title = 'student'

	# 实例变量
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


class Animal(object):

	def run(self):
		print('animal is running')


class Dog(Animal):

	def __init__(self, *args, **kwargs):
		self.__args = args
		self.__kwargs = kwargs

	def run(self, ):
		print('dog is running')

	def get_args(self):
		return self.__args

	def get_kwargs(self):
		return self.__kwargs


class Cat(Animal):

	def run(self):
		print('cat is running')


def run_twice(animal_twice):
	animal_twice.run()
	animal_twice.run()


class Timer(object):

	def run(self):
		print('start........')


if __name__ == '__main__':
	student = Student('sage', 24, 'HeBei')
	student.get_info()
	print(student.get_age_level())

	dog = Dog('dog', 34, address='he')
	print(dog.get_args())
	print(dog.get_kwargs())
	dog.run()
	cat = Cat()
	cat.run()
	print('is dog is Dog? ', isinstance(dog, Dog))
	print('is dog is Animal? ', isinstance(dog, Animal))
	animal = Animal()
	animal.run()
	print('----------------------')
	run_twice(dog)
	run_twice(cat)
	run_twice(Animal())
	# feel like an object(传入的参数不是animal类型也可以，只要有run方法即可)
	run_twice(Timer())

	print(type(lambda x: x) == types.LambdaType)
	print(type(cat))
	print(type(dog))
	print(type(animal))
	print(isinstance(cat, Cat))
	print(isinstance(cat, Animal))
	print(isinstance(dog, (Dog, Animal)))
	print(dir(str))

	print(hasattr(cat, 'name'))
	setattr(cat, 'name', 'cute cat')

	print(hasattr(student, 'name'))
	print(student.name)
	setattr(student, 'name', 'zhangsan')
	print(student.name)
	print(getattr(student, 'name'))
	print(getattr(student, 'address'))
	print(Student.title)
	print(student.title)
