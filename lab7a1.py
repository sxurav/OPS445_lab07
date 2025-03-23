#!/usr/bin/env python3
# Student ID: sourav1
from lab7a import *

# Create time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Time difference to add
td = Time(0, 50, 0)

# Sum the times
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
tsum3 = sum_times(t3, td)

# Format and print the results
print(format_time(t1), '+', format_time(td), '-->', format_time(tsum1))
print(format_time(t2), '+', format_time(td), '-->', format_time(tsum2))
print(format_time(t3), '+', format_time(td), '-->', format_time(tsum3))
