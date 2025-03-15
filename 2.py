def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            return max(words, key=len) if words else None
    except FileNotFoundError:
        return "File not found."


print(find_longest_word("file1.txt"))  
