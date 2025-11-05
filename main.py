from stats import get_num_words
from stats import dict_to_list


class custom_iterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    book = get_book_text("./books/frankenstein.txt")

    iterable_dict = custom_iterable(dict_to_list(book))

    list_string = ""
    for dicts in iterable_dict:
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
