filename = input('Enter name of the file: ')
try:
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        print(f"Number of lines: {len(lines)}")
        print(f"Number of characters: {len(content)}")
        words = 0
        for word in lines:
            words += 1
        print(f"Number of words: {words}")
except FileNotFoundError:
    print("That file does not exist.")