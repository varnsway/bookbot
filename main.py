def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(filepath):
    count = 0
    with open(filepath) as f:
        file_contents = f.read()
        words_split = file_contents.split()
        for i in words_split:
            count += 1
    return count

def main():
    count = get_word_count("books/frankenstein.txt")
    #text = get_book_text("books/frankenstein.txt")
    print(f"{count} words found in the document")

main()
