from datetime import datetime

# Define the date and time
previous_date_time = datetime(1970, 1, 1)
current_date_time = datetime.now()

# compare the date time
time_difference_in_seconds = (current_date_time - previous_date_time).total_seconds()

# Convert the date string to a datetime object
previous_date_time_obj = previous_date_time.strftime("%B %d, %Y")
current_date_time_obj = current_date_time.strftime("%b %d %Y")

# Format the datetime object as a string
format_time_result = f"Seconds since {previous_date_time_obj}: {time_difference_in_seconds:.4f} or {time_difference_in_seconds:.2e} in scientific notation"

#printing the result
print(format_time_result)
print(current_date_time_obj)
