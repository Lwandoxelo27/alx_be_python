# Prompt for a Single Task
task = input("Enter a task description: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        priority_message = "High priority"
    case "medium":
        priority_message = "Medium priority"
    case "low":
        priority_message = "Low priority"
    case _=
        priority_message = "Unknown priority"

if time_bound.lower() == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = ""

# Provide a Customized Reminder
print(f"Reminder: {task} - {priority_message}{time_message}")