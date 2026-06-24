import os

def create_and_write_file(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(content)
    return "File created and written successfully!"

def read_file_content(filename):
    if not os.path.exists(filename):
        return "Error: File does not exist!"
    with open(filename, 'r') as f:
        return f.read()

def append_to_file(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write("\n" + content)
    return "Content appended successfully!"