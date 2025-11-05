def num_words(content):
    word_count = 0
    for word in content.split():
        word_count += 1
    return word_count


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    book = get_book_text("./books/frankenstein.txt")
    print(f"Found {num_words(book)} total words")


main()
