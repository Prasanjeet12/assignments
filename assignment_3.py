# Task_1
def factorial(n):
    """Calculate factorial of a given number"""
    if n < 0:
        return "Factorial does not exist for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))

print(f"Factorial of {number} is: {factorial(number)}")

#Task_2
import math

number = float(input("Enter a number: "))

sqrt_value = math.sqrt(number) if number >= 0 else "Square root not defined for negative numbers"
log_value = math.log(number) if number > 0 else "Logarithm not defined for zero or negative numbers"
sine_value = math.sin(number)  # Sine takes input in radians

print(f"\nResults for the number {number}:")
print(f"Square root: {sqrt_value}")
print(f"logarithm: {log_value}")
print(f"Sine: {sine_value}")
