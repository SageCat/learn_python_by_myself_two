#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
from functools import partial


def func(x, y, f):
	return f(x) + f(y)


def positive(num):
	if num > 0:
		return num
	else:
		return -num


def is_odd(n):
	return n % 2 == 0


def odd_iter():
	n = 1
	while True:
		n += 2
		yield n


def not_divisible(n):
	return lambda x: x % n > 0


def primes():
	yield 2
	it = odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(not_divisible(n), it)


def by_name(t):
	key_contents = []
	for key in t:
		key_contents.append(key[0])
	return key_contents


def lazy_sum(*args):
	def sum():
		ax = 0
		for i in args:
			ax = ax + i
		return ax

	return sum


def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i

		fs.append(f)
	return fs


def count_two():
	def f(j):
		def g():
			return j * j

		return g

	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs


def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def build(x, y):
	return lambda: x * x + y * y


# print(abs)
# a = -10
# print(abs(-10))
# # 函数名也是变量，是指向函数的变量
# print(func(-3, 4, abs))
# print(func(-4, -5, positive))
# # map第一个参数是函数
# # 第二个参数是一个序列
# # map将第一个参数的函数作用到序列的每一个元素上并返回一个Iterator
# result = map(abs, [-1, 2, -90, -56.3, 67])
# print(type(result))  # map类型
# print(result)
# print(next(result))  # 具有迭代器Iterator的特性
# print(list(result))  # 将返回的Iterator转换为序列
#
# result_two = map(str, (1, 2, 3, 4, 5, 6))
# print(result_two)
# print(next(result_two))
# print(list(result_two))
# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# f = open("/Users/sage/PycharmProjects/learn_python_02/primes.txt", 'w')
# for n in primes():
# 	if n < 10:
# 		print(n)
# 		f.write(str(n) + '\r\n')
# 	else:
# 		f.close()
# 		break
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=itemgetter(0))
# print(L2)
# f = lazy_sum(1, 2, 3, 4, 5)
# print(f)
# print(f())
# f1, f2, f3 = count_two()
# print(f1())
# print(f2())
# print(f3())
#
# print(build(1, 2)())


def outer():
	x = 1
	y = 2

	# 函数的闭包，只有在inner中被调用的outer变量，才会被记录到封闭作用域中
	def inner():
		print(x)

	return inner


def outer_func(some_func):
	def inner():
		print('before some_func')
		r = some_func()
		return r + 1
	return inner


def foo():
	return 2


# 一般装饰器都写两层，返回一个句柄，为了防止不显示调用时封装器也会被调用
def wrapper(func):
	def inner():
		print('before func---1')
		# func()
		func()
		print('func name is ', func.__name__)
		print('after func----1')
	return inner


def wrapper2(func):
	def inner():
		print('before func---2')
		# func()
		func()
		print('func name is ', func.__name__)
		print('after func----2')
	return inner


# 带有两个参数的装饰器
def wrapper_with_parameter(func):
	def inner(a, b):
		print('before inner')
		print('sum is ', func(a, b))
		print('after inner')
	return inner


def wrapper_with_multi_parameter(func):
	def inner(*args, **kwargs):
		print('before inner')
		result = func(*args, **kwargs)
		print('the value of %s is %d'%(func.__name__, result))
		print('after inner')
	return inner


@wrapper_with_parameter
def func_with_parameter(a, b):
	return a + b


@wrapper_with_multi_parameter
def func_sum_two_num(a, b):
	return a + b


@wrapper_with_multi_parameter
def func_sum_three_num(a, b, c):
	return a + b + c


# def wrapper(func):
# 	print('before func')
# 	# func()
# 	print(func.__name__)
# 	print('after func')
# 	return func


@wrapper2
@wrapper
def func1():
	print('func 1------')


# decorate = outer_func(foo)
# decorate_two = outer_func(decorate)
# print(decorate)
# decorate()
# print(decorate_two)
# decorate_two()
print('----------------')
# decorate = wrapper(func1)
# decorate_two = wrapper(decorate)
# print(decorate)
# decorate()
# print(decorate_two)
# decorate_two()
# func1()
func_with_parameter(1, 2)
print('----------------')
func_sum_two_num(3, 4)
print('----------------')
func_sum_three_num(1, 2, 8)

# use functools中的偏函数
int_binary = partial(int, base=8)
print(int_binary('101000'))


