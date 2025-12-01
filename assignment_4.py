# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


# Task 2: Write to a File

text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display the final file content
print("Final content of output.txt:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)