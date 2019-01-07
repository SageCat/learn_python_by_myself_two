#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

from operator import itemgetter


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


print(abs)
a = -10
print(abs(-10))
# 函数名也是变量，是指向函数的变量
print(func(-3, 4, abs))
print(func(-4, -5, positive))
# map第一个参数是函数
# 第二个参数是一个序列
# map将第一个参数的函数作用到序列的每一个元素上并返回一个Iterator
result = map(abs, [-1, 2, -90, -56.3, 67])
print(type(result))  # map类型
print(result)
print(next(result))  # 具有迭代器Iterator的特性
print(list(result))  # 将返回的Iterator转换为序列

result_two = map(str, (1, 2, 3, 4, 5, 6))
print(result_two)
print(next(result_two))
print(list(result_two))
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = open("/Users/sage/PycharmProjects/learn_python_02/primes.txt", 'w')
for n in primes():
	if n < 10:
		print(n)
		f.write(str(n) + '\r\n')
	else:
		f.close()
		break

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=itemgetter(0))
print(L2)
f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())
f1, f2, f3 = count_two()
print(f1())
print(f2())
print(f3())

print(build(1, 2)())
