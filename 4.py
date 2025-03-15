def reverse_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        with open("reversed.txt", 'w') as new_file:
            new_file.write(content[::-1])
    except FileNotFoundError:
        print("File not found.")

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None


reverse_file_content("file1.txt")

print(read_file_content("reversed.txt"))
