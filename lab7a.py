#!/usr/bin/env python3
# Student ID: sourav1

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    # Sum the seconds, minutes, and hours separately
    total_seconds = t1.second + t2.second
    total_minutes = t1.minute + t2.minute
    total_hours = t1.hour + t2.hour
    
    # Handle overflow of seconds into minutes
    if total_seconds >= 60:
        total_minutes += total_seconds // 60
        total_seconds %= 60

    # Handle overflow of minutes into hours
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes %= 60

    # Hours should not exceed 24, roll over to next day if necessary
    total_hours %= 24

    # Create a new Time object with the summed values
    return Time(total_hours, total_minutes, total_seconds)

def valid_time(t):
    """Check for the validity of the time object attributes:
        0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def main():
    # Example time objects
    time1 = Time(8, 55, 30)  # 08:55:30
    time2 = Time(1, 15, 45)  # 01:15:45

    # Summing times
    result = sum_times(time1, time2)
    print(f'{format_time(time1)} + {format_time(time2)} = {format_time(result)}')

    # Check if a time object is valid
    if valid_time(result):
        print(f'{format_time(result)} is a valid time.')
    else:
        print(f'{format_time(result)} is not a valid time.')

if __name__ == '__main__':
    main()
