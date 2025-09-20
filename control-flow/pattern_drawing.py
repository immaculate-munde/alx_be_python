try:
    size = int(input("Enter the size of the pattern: "))

    if size > 0:
        row = 0
        # Outer while loop for rows
        while row < size:
            # Inner for loop for columns
            for col in range(size):
                print("*", end="")  # Print without newline
            print()  # Move to the next line after each row
            row += 1
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")