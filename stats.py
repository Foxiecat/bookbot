class Stats:
    def __init__(self, content):
        self.content = content

    def get_word_count(self):
        word_count = 0
        for word in self.content.split():
            word_count += 1
        return word_count

    def get_character_count(self):
        char_count = {}
        for character in self.content.lower():
            if character in char_count:
                char_count[character] += 1
                continue
            char_count[character] = 1
        return char_count

    @staticmethod
    def sort_on(items):
        return items["num"]

    def dict_to_list(self):
        list_of_dicts = []
        character_dict = self.get_character_count()
        for key, value in character_dict.items():
            list_of_dicts.append({"char": key, "num": value})
        return sorted(list_of_dicts, reverse=True, key=self.sort_on)
