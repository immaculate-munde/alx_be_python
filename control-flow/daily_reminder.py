# Prompt for user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process task based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a HIGH priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Check if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"

elif priority in ["high", "medium", "low"]:
    # Add a suggestion only if priority was valid
    message += ". Consider completing it when you have free time."

# Output the final reminder
print("\n" + message)