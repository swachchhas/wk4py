def check_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            return len(file.read().strip()) == 0
    except FileNotFoundError:
        return "File not found."



print(check_file_empty("file1.txt"))  
print(check_file_empty("empty.txt"))  
