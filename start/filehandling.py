def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

def count_letters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        letters = [char for char in content if char.isalpha()]
        return len(letters)

def manipulate_sentences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        sentences = content.split('.')
        manipulated_sentences = [sentence.strip().upper() for sentence in sentences]
        return '. '.join(manipulated_sentences)

# Example usage
file_path = '/path/to/your/file.txt'

# Word count
word_count = count_words(file_path)
print(f"Word count: {word_count}")

# Letter count
letter_count = count_letters(file_path)
print(f"Letter count: {letter_count}")

# Sentence manipulation
manipulated_content = manipulate_sentences(file_path)
print(f"Manipulated content: {manipulated_content}")