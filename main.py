from stats import get_num_words
from stats import dict_to_list


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    book = get_book_text("./books/frankenstein.txt")

    list_string = ""
    for dicts in dict_to_list(book):
        for key, value in dicts:
            if not key.isalpha():
                continue
            list_string += f"{key}: {value}\n"

    report = f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {get_num_words(book)} total words
    --------- Character Count -------
    {list_string}
    ============= END ===============
    """

    print(report)


main()
