students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Emma": 88
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print("Student not found in the records.")


#Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))


first_five = numbers[:5]

#  Reverse the extracted elements
reversed_list = first_five[::-1]

#  Print both lists
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_list)