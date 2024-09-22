# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("This is the second line, with a number: 123.\n")
        file.write("Finally, this is the third line.\n")
    print("File 'my_file.txt' created and written successfully.")

except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation attempt completed.")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print("\nContents of 'my_file.txt':")
        print(contents)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading attempt completed.")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending a new line to the file.\n")
        file.write("Adding another line with a number: 456.\n")
        file.write("This is the last appended line.\n")
    print("New lines appended to 'my_file.txt' successfully.")

except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending attempt completed.")