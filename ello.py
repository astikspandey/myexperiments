# Opening a file
file = open('executer.py', 'r')

# Perform file operations
content = file.read()
print(content)

# Close the file without quitting the Python program
file.close()

# Program continues to run
print("File is closed, but the program is still running.")
input()
