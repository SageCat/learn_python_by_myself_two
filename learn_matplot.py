#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
fig.suptitle('sage')
# fig, ax_list = plt.subplots()
x = np.linspace(0, 2, 100)
plt.plot(x, x**2, label='x**2')
plt.plot(x, x**3, label='x**3')
plt.legend()
plt.show()
