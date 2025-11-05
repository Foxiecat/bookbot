def get_num_words(content):
    word_count = 0
    for word in content.split():
        word_count += 1
    return word_count


def get_character_count(content):
    char_count_dect = dict()
    for character in content.lower():
        if character in char_count_dect:
            char_count_dect[character] += 1
            continue
        char_count_dect[character] = 1
    return char_count_dect


def sort_on(items):
    return items["num"]


def dict_to_list(content):
    list_of_dicts = []
    character_dict = get_character_count(content)
    for key, value in character_dict:
        list_of_dicts.append({"char": key, "num": value})
    return list_of_dicts.sort(reverse=True, key=sort_on)
