# daily_reminder.py
# Single-task daily reminder using match-case and conditional modification for time-bound tasks

# Prompt for a single task
task = input("Enter your task: ").strip()

# Prompt for priority and time-bound status
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# React based on priority using match-case and modify the reminder if time-bound
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            # low priority but time-bound — still flag as note since example output used "Note:" for low
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        # Unknown priority: still provide guidance and respect time-bound flag
        if time_bound == "yes":
            print(f"Reminder: '{task}' has an unknown priority level that requires immediate attention today!")
        else:
            print(f"'{task}' has an unknown priority level. Consider specifying high, medium, or low.")
