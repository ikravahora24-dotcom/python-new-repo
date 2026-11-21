
def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        return "File not found"


print(read_file_safely("sample.txt"))
