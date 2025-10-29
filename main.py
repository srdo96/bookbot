from stats import count_words, num_of_each_character, sort_dict
import sys

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    arg = sys.argv
    if len(arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = arg[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = num_of_each_character(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    sorted_list = sort_dict(char_dict)
    for e in sorted_list:
       if not e["char"].isalpha():
           continue
       print(f"{e["char"]}: {e["num"]}")
    print("============= END ===============")

main()
