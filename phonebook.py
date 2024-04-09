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

from csv import DictReader, DictWriter  # Импортируем методы DictReader и DictWriter из модуля csv
from os.path import exists

patronymic = 'Urievich'

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


def create_file(file_path):
    # with - Менеджер контекста
    with open(file_path, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_path, lst):
    res = read_file(file_path)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_path, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copying_string(file_path, my_str):
    num_str = int(input('Введите номер строки для копирования: ')) - 1
    if num_str > len(my_str) - 1 or num_str < 0:
        print('Такой строки нет')

    else:
        my_str = my_str[num_str]
        res = read_file(file_path)
        for el in res:
            if el["Телефон"] == my_str["Телефон"]:
                print("Такая строка уже есть")
                return

        res.append(my_str)
        with open(file_path, "w", encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)


file_name = 'phone.csv'
file_name_2 = 'important_phone.csv'

def main():
    print('Команды: \n q-выход \n w-запись \n r-вывод \n c-копирование')
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'c':
            if not exists(file_name_2):
                create_file(file_name_2)
            lst_2 = read_file(file_name)
            copying_string(file_name_2, lst_2)
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
            print('Новвый файл')
            print(*read_file(file_name_2))


main()
