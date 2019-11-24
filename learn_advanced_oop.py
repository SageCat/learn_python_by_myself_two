#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
from types import MethodType
import numpy as np


class Student(object):
    # __slots__ = ('name', 'set_name', 'get_name')

    def __init__(self):
        pass

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


def set_name(self, name):
    self.name = name


def get_name(self):
    return self.name


class ClassWithSlots(object):
    # 只能有__slots__指定的参数，具有其他参数会报错，可节约百分之40~50内存
    __slots__ = ('name', 'age', 'address')

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class TestPrivate(object):
    def __init__(self, width, height, resolution):
        self._width = width
        self._height = height
        self.__resolution = resolution

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_resolution(self):
        return self.__resolution

    def set_resolution(self, resolution):
        self.__resolution = resolution


class TestProperty(object):
    def __init__(self, language, address):
        self._language = language
        self._address = address

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        if language == 'Chinese':
            raise ValueError('language should not be Chinese')
        self._language = language

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address


if __name__ == '__main__':
    s = Student()
    # 为实例绑定属性
    s.name = 'sage'
    print('name is ', s.name)

    # 为实例绑定方法
    s.set_name = MethodType(set_name, s)  # 等同于 s.set_name = set_name
    s.get_name = MethodType(get_name, s)
    s.set_name('guo')
    print('the name got is', s.get_name())

    # 为类绑定方法，这样所有的实例就都有相同的方法了
    Student.set_name = MethodType(set_name, Student)  # 等同于 Student.set_name = set_name
    s2 = Student()
    s2.set_name('student 2')
    print('name is', s2.name)
    print(np.version)
    s.set_score(23)
    print(s.get_score())

    with_slots = ClassWithSlots('sage', 23, 'ss')
    print(with_slots.name, with_slots.age, with_slots.address)
    print("================================")

    private_demo = TestPrivate(23, 45, 100)
    print('height is', private_demo.get_height())
    print('width is', private_demo.get_width())
    print('resolution is', private_demo.get_resolution())
    private_demo._width = 29
    print('width is', private_demo.get_width())
    # 此行为为对象动态绑定了一个名为'__resolution'的变量，并不能改变初始化的成员变量
    private_demo.__resolution = 200
    print('resolution is', private_demo.get_resolution())  # 成员变量依然为100
    print('__resolution is', private_demo.__resolution)  # __resolution变量为200
    private_demo.set_resolution(300)  # 通过set方法为私有的resolution修改值，其实私有变量为_TestPrivate__resolution
    print('resolution is', private_demo.get_resolution())  # get方法得到的私有的resolution的值为300,已被set方法修改
    print("================================")

    property_demo = TestProperty('English', 'Hebei')
    print('property_demo language is', property_demo.language)
    print('property_demo address is', property_demo.address)
    # property_demo.language = 'Chinese'  # 报错，提示语言不能设置为Chinese
    property_demo.language = 'Spanish'
    print('property_demo language is', property_demo.language)
