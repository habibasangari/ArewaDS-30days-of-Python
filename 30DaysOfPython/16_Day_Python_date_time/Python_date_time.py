#  Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

current_datetime = datetime.now()  # Get current date and time

current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute

timestamp = current_datetime.timestamp()  # Get timestamp

print(f"Current Date: {current_day}-{current_month}-{current_year}")
print(f"Current Time: {current_hour}:{current_minute}")
print(f"Timestamp: {timestamp}")


# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime

current_datetime = datetime.now()

formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")  # Format the date and time
print("Formatted Date:", formatted_date)


#  Today is 5 December, 2019. Change this time string to time.

from datetime import datetime

time_string = "5 December, 2019"

formatted_datetime = datetime.strptime(time_string, "%d %B, %Y") # Convert time string to datetime object

print("Formatted Datetime:", formatted_datetime)


#  Calculate the time difference between now and new year.
from datetime import datetime, timedelta

current_datetime = datetime.now()

new_year_date = datetime(current_datetime.year + 1, 1, 1, 0, 0, 0)

time_difference = new_year_date - current_datetime  # Calculate the time difference
print("Time difference until New Year:", time_difference)


# Calculate the time difference between 1 January 1970 and now.

from datetime import datetime

current_datetime = datetime.now()

epoch_date = datetime(1970, 1, 1, 0, 0, 0)  # Set the Unix epoch date

time_difference = current_datetime - epoch_date

print("Time difference since January 1, 1970:", time_difference)


'''Time Series Analysis: The datetime module is crucial for working with time series data. 
It allows you to manipulate and analyze temporal data efficiently.

Logging and Timestamps: You can use the datetime module to timestamp events 
or log entries in applications.This is especially useful for tracking when
specific activities occurred.

Web Development: In web development, you might use the datetime module to manage 
dates and times related to various aspects, such as blog posts, user activity, or scheduled events.
'''


