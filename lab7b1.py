#!/usr/bin/env python3
# Student ID: sourav1
from lab7b import *

t1 = Time(9, 50, 0)
format_time(t1)

seconds = 1800
change_time(t1, seconds)
print(format_time(t1))

seconds = -1800
change_time(t1, seconds)
print(format_time(t1))
