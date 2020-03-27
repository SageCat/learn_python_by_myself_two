#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo

for i in range(16):
    print("{0:^2} the value is {0:>02x}".format(i))

print(0b11)
print(0x22)

# %%
print("----------------------------------------------------------------")
print("{:>5} {:^10} {:^10} {:^10} the value is".format(10, 1, 4, 23))
# %%
# 0x represents hex, 0o represents octal
x = 0x20
y = 0x0a
z = 0o10
print(x)
print(y)
print(z)
print(x * y)

print(0b10011100, end='')
