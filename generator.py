#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

"""
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
"""

from collections import Iterable
from collections import Iterator


# fib function to generator fib numbers
def fib(max_value):
	n, a, b = 0, 0, 1
	while n < max_value:
		# print(b)
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'


def add(x, y, f):
	return f(x) + f(y)


list_01 = [x * x for x in range(1, 10)]
print(list_01)
print(type(list_01))

generator_01 = (x * x for x in range(20))
print(generator_01)
print(type(generator_01))

x = fib(20)
print(type(x))
print('---------------------')
for y in x:
	print(y)

print('if x is Iterable ?', isinstance(x, Iterable))  # True
print('if x is Iterator ?', isinstance(x, Iterator))  # True

for i in [1, 2, 3, 4, 5]:
	print('i is ', i)
print('>>>>>>>>>>>>>>>>>')
for i in iter([1, 2, 3, 4, 5]):
	print('i is ', i)

it = iter([1, 2, 3, 4, 5, 6, 7])
while True:
	try:
		print('next value is', next(it))
	except StopIteration:
		print('it is the end')
		break
f = abs
print(f)
print(type(abs))

print(add(-5, 6, abs))

hello = 'hello sage'
print(type(hello))
print(type(list(hello)))
print(type(set(hello)))
print(type(tuple(hello)))

test_str = "sage", "name", 17
print(test_str)
print(type(test_str))

test_str_02 = {'sage', 'name', 17}
# print(test_str_02)
for i in test_str_02:
	print(i)
print(type(test_str_02))

test_str_03 = ['sage', 'guo', 'name']
print(test_str_03.sort())  # 方法返回None
print(test_str_03)
