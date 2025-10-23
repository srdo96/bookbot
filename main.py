from stats import count_words, num_of_each_character

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dic = num_of_each_character(text)
    print(f"Found {num_words} total words")

    for char in char_dic:
        print(f"'{char}': {char_dic[char]}")
main()

