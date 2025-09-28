from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(days):
    current_date = datetime.now()
    # Add the specified number of days
    future_date = current_date + timedelta(days=days)
    # Format as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

def main():
    # Part 1: Show current date and time
    display_current_datetime()
    
    # Part 2: Ask user for days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
