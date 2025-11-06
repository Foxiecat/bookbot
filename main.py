from stats import Stats
import sys


class BookBot:
    def run(self):
        if len(sys.argv) == 1:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        book = get_book_text(sys.argv[1])
        stats = Stats(book)

        char_list = stats.dict_to_list()

        list_string = ""
        for dictionary in char_list:
            char = dictionary["char"]
            num = dictionary["num"]
            if not char.isalpha():
                continue
            list_string += f"{char}: {num}\n"

        report = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {stats.get_word_count()} total words
--------- Character Count -------
{list_string}
============= END ===============
"""
        print(report)
        sys.exit(0)


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


if __name__ == "__main__":
    app = BookBot()
    app.run()
