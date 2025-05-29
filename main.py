from stats import get_word_count
from stats import char_count
from stats import d_list

def main():
    count = get_word_count("books/frankenstein.txt")
    #text = get_book_text("books/frankenstein.txt")
    #print(f"{count} words found in the document")
    #char_count("books/frankenstein.txt")
    d = char_count("books/frankenstein.txt")
    x = d_list(d)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in x:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
main()