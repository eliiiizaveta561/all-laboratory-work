#задание 1
# with open('example', 'r', encoding='utf-8') as file:
#     content = file.read()
# print(content)


# def read_file(file_path, read_mode):
#     with open(file_path, 'r', encoding = 'utf-8') as file:
#         if read_mode == 'all':
#             content = file.read()
#             print(content)
#         elif read_mode == 'line':
#             for line in file:
#                 print(line)
#         else:
#             print('Неверный режим для чтения')
# read_file("example", 'line')


#задание 2
# text = input('Введите текст: ')
# with open('user_input', 'a', encoding='utf-8') as file:
#     file.write(text + '\n')
#     print('Текст записан')


#задание 3
# def read_file(file_path, read_mode):
#     try:
#         with open(file_path, 'r', encoding = 'utf-8') as file:
#             if read_mode == 'all':
#                 content = file.read()
#                 print(content)
#             elif read_mode == 'line':
#                 for line in file:
#                     print(line, end = '')
#             else:
#                 print('Неверный режим чтения')
#     except FileNotFoundError:
#         print('Ошибка: файл не найден')
# read_file("example", 'all')

