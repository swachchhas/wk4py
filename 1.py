def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



write_to_file("file1.txt", "Hello, this is a sample text.")
print(read_file_content("file1.txt"))  