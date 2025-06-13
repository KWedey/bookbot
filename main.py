from stats import get_num_words, count_char, sorted
import sys

def main():
    if len(sys.argv) != 2: 
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = count_char(text)
    # print(f"{num_words} words found in the document")
    # print(num_chars)
    sorted_list = sorted(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        letter = dict["char"]
        if letter.isalpha():
            print(f"{letter}: {dict['num']}")
    print("--------- END -------")




def get_book_text(path):
    with open(path) as f:
        return f.read()


main()