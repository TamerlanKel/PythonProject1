# import io
# from pprint import pprint
#
# name = 'test.txt'
# file = open(name, 'r', encoding='utf-8')
# print(file.writable())
# print(file.readable())
# print(file.seekable())
# print(file.closed)
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# file.close()


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding= 'utf-8')
    line_number = 1
    for string in strings:
        bite_position = file.tell()
        file.write(string + '\n')
        strings_positions[(line_number, bite_position)] = string
        line_number += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)