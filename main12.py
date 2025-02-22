# Import the math module to use sqrt function
import math

# Function to calculate the square root
def calculate_square_root(number):
    if number < 0:
        return "Error: Cannot take the square root of a negative number."
    else:
        return math.sqrt(number)

# Main code
if __name__ == "__main__":
    try:
        # Ask the user for a number
        num = float(input("Enter a number to find the square root: "))
        # Call the function and print the result
        result = calculate_square_root(num)
        print(f"The square root of {num} is {result}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")