# Create a program that reads a file and writes a modified version to a new file.
# File Read & Write Challenge
try:
    with open("input.txt", "r") as infile:
        content = infile.read()
    # modification: convert text to uppercase
    modified_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)
    print(" File has been read and modified version written to output.txt")
except FileNotFoundError:
    print("input.txt not found. Please create the file and try again.")


# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename = input("Enter the filename to read: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except PermissionError:
    print(f"You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


