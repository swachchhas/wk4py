
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."



def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



def process_file_with_lambda(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file: 
            for line in lines:
                file.write(' '.join(map(lambda word: word.upper(), line.split())) + '\n')

    except FileNotFoundError:
        print("File not found.")



write_to_file("file1.txt", "Hello world\nPython is awesome")
process_file_with_lambda("file1.txt")
print(read_file_content("file1.txt")) 