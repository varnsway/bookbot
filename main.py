from stats import get_word_count
from stats import char_count
from stats import d_list
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        count = get_word_count(sys.argv[1])
        d = char_count(sys.argv[1])
        x = d_list(d)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for i in x:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
    
main()