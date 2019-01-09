#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
import copy


def get_memory_address(variable):
	return 'variable memory address is: ' + hex(id(variable))


def print_spilt():
	print('-------------------')


age = [12, 34, 56, [1, 2, 3, 4, 5]]
# = 默认进行浅复制，只copy了地址，其中任一变量改变，会导致所有使用同一地址的变量发生改变
age_copy = age
# 地址一致
print(get_memory_address(age))
print(get_memory_address(age_copy))
age_copy.append(23)
print('age is ', age)
print('age_copy is ', age_copy)
age[3].append(300)
print('age is ', age)
print('age_copy is ', age_copy)

print_spilt()
age_copy_two = copy.copy(age)
print(get_memory_address(age))
print(get_memory_address(age_copy_two))
age.append(90)
print('original value is: ', age)
print('shallow copy value is :', age_copy_two)
age[3].append(100)
print('original value is: ', age)
print('shallow copy value is :', age_copy_two)

print_spilt()
age_deep_copy = copy.deepcopy(age)
print(get_memory_address(age))
print(get_memory_address(age_deep_copy))
age.append(1000)
print('original value is: ', age)
print('deep copy value is :', age_deep_copy)
age[3].append(999)
print('original value is: ', age)
print('deep copy value is :', age_deep_copy)
