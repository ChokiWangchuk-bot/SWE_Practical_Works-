def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:100])  

def count_lines(content):
    return len(content.splitlines())


num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")


