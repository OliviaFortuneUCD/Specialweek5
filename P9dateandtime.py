# Python3 code to demonstrate
# attributes of now() for timezone

# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('America/New_York'))

# printing current time in india
print("The current time in New York is : ")
print(current_time)