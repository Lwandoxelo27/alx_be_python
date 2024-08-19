from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    days = int(input("Enter the number of days: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print("Future Date:", future_datestrftime("%Y-%m-%d"))

# Call the functions
display_current_datetime()
calculate_future_date()
