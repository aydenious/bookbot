import sys
import os
from stats import count_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
      file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    length = count_words(text)
    print(f"Found {length} total words")

    print("--------- Character Count -------")

    character_count = count_characters(text)

    sorted_char_list = sort_characters(character_count)

    for item in sorted_char_list:
        print(f"{item['char']}: {item['count']}")

    print("============ END ============")


main()


