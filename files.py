# file_handling_assignment.py

# File creation and writing
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is line 1.\n")
        file.write("Here is number 42 on line 2.\n")
        file.write("Another string on line 3.\n")
    print("File created and written successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# File reading and displaying
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nReading file contents:\n")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied when trying to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 4.\n")
        file.write("Appending number 99 on line 5.\n")
        file.write("Final appended string on line 6.\n")
    print("\nFile appended successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final file reading after appending
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nFinal file contents after appending:\n")
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file after appending: {e}")
