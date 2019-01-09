#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

ages = {'michael': 25, 'brandy': 26, 'sue': 29, 'aria': 22}
ages_key = ages.keys()
print(ages_key)
result = sorted(ages, key=ages.get)
print(result)
