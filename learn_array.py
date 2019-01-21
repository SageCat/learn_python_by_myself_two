#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
import numpy as np

array_one = np.array([[1, 2], [3, 6]])
print(array_one)
array_one_inverse = np.linalg.inv(array_one)
print(array_one_inverse)
