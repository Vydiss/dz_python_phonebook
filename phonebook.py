"""
Задача №49. Общее обсуждение.
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
5. Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
6. Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""

from csv import DictReader, DictWriter # Импортируем методы DictReader и DictWriter из модуля csv
from os.path import exists

patronymic = 'Urievich'
file_name = 'phonebook.csv'

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class InvalidNameError(Exception):
    def __init__(self, txt):
        self.txt = txt

#
def get_info():
    """
    Функция для получения и проверки данных от пользователя
    \n пользовательский ввод
    :return:
    """
    first_name = None
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise InvalidNameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except InvalidNameError as err:
            print(err)
            continue

    last_name = None
    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилью: ")
            if len(last_name) < 2:
                raise InvalidNameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except InvalidNameError as err:
            print(err)
            continue

    phone_number = None
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def file_app():
    with open('phonebook.csv') as f_n:
        pass