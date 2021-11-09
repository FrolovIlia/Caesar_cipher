entry_direction = input('Что нужно сделать: шифровать или дешифровать? \n').lower()
while entry_direction != 'шифровать' and entry_direction != 'дешифровать':
    entry_direction = input('Не корректное значение. Напишите "шифровать" или "дешифровать". \n').lower()

entry_language = input('Какой язык использовать: русский или английский?\n').lower()
while entry_language != 'русский' and entry_language != 'английский':
    entry_language = input('Не корректное значение. Напишите "русский" или "английский". \n').lower()

entry_step = input('На сколько сдвигаем шифр?: Введите число \n')
while entry_step.isdigit() != True:
    entry_step = input('Не корректное значение. Введите число. \n')

entry_text = input('Введите текст для обработки \n')
while entry_text.isspace() == True:
    entry_text = input('Не корректное значение. Введите текст. \n')


def start(direction, language, step, text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):
        # Задаем локальные переменные: длину алфавита и значения словарей.
        if language == 'русский':
            abc = 32
            low_abc = lower_rus_alphabet
            up_abc = upper_rus_alphabet
        if language == 'английский':
            abc = 26
            low_abc = lower_eng_alphabet
            up_abc = upper_eng_alphabet

        # Если text[i] является буквой:
        if text[i].isalpha():

            # Находим место символа text[i] в словаре upper_alphabet либо lower_alphabet.
            if text[i] == text[i].lower():
                place = low_abc.index(text[i])
            if text[i] == text[i].upper():
                place = up_abc.index(text[i])

            # Если нужно дешифровать, то:
            if direction == 'дешифровать':
                # Находим индекс для измененного символа.
                index = (place - int(step)) % abc

            # Если нужно зашифровать, то:
            elif direction == 'шифровать':
                # Находим индекс для измененного символа.
                index = (place + int(step)) % abc

            # Выводим измененный символ.
            if text[i] == text[i].lower():
                print(low_abc[index], end='')
            if text[i] == text[i].upper():
                print(up_abc[index], end='')

            # Если text[i] не является буквой:
        else:
            print(text[i], end='')


start(entry_direction, entry_language, entry_step, entry_text)
