# import io
# from pprint import pprint
#
# name = 'file3.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         for char in line:
#             print(char, end='')
#     print(file.tell())
# print(file.read())

import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = {*file_names}

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punctuation, '')
                words = line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
            else:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        counts = {}
        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word)  
        return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
