"""
Datetime
A date in Python is not a data type of its own, but we can import a module
named datetime to work with dates as date objects.

"""

# Import the datetime module and display the current date:
import datetime

getdate = datetime.datetime.now()
print(getdate)

# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.

print(getdate.year)
print(getdate.strftime("%A"))
print(getdate.strftime("%B"))
print(getdate.strftime("%c"))
print(getdate.strftime("%x"))