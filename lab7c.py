#!/usr/bin/env python3
# Student ID: sourav1

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

def time_to_sec(t):
    """Convert time object to total seconds."""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    hour = (seconds // 3600) % 24  # Get the hour, make sure it's within 24 hours
    minute = (seconds % 3600) // 60  # Get the minute within 0-59
    second = seconds % 60  # Get the second within 0-59
    return Time(hour, minute, second)

def change_time(t, seconds):
    """Change the time by adding the specified number of seconds."""
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second + seconds
    t.hour = (total_seconds // 3600) % 24  # Ensure hour stays within 24
    t.minute = (total_seconds % 3600) // 60  # Ensure minute is within 0-59
    t.second = total_seconds % 60  # Ensure second is within 0-59

# Example usage:
t3 = Time(8, 30, 0)
change_time(t3, 1800)  # Add 1800 seconds (30 minutes)

# Output the modified time
print(format_time(t3))  # Should print 09:00:00

# Example for sec_to_time:
total_seconds = 5400  # Example of total seconds
time_obj = sec_to_time(total_seconds)
print(format_time(time_obj))  # Should print 01:30:00 (5400 seconds)
