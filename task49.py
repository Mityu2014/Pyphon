""" Задача №49. Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
 """


from csv import DictReader, DictWriter
from os.path import exists
 
class LenError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid = False
    while not is_valid:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise LenError("Короткое имя")
            else:
                last_name = input("Введите фамилию: ")
                if len(first_name) < 2:
                    raise LenError("Короткая фамилия")
                else:
                    phone_number = int(input("Введите номер: "))
                    if len(str(phone_number)) != 11:
                        raise LenError("Невалидная длина")
                    else:
                        is_valid = True
        except LenError as err:
            print(err)
            continue
        except ValueError:
            print("Невалидный номер")
            continue
    return {'имя': first_name, 'фамилия': last_name, 'телефон': phone_number}

def get_copy():
    res = read_file(file_name)
    is_valid = False
    while not is_valid:
        try:
            num_row = int(input("Введите номер строки для копирования: "))-1
            if len(res) < num_row:
                raise LenError("Такой строки нет")
            else:
                is_valid = True
        except LenError as err:
            print(err)
            continue
        except ValueError:
            print("некорректное значение строки")
            continue
    return res[num_row]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя','фамилия', 'телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file,command):
    res = read_file(file)
    if command == 'w':
        obj = get_info()
    else:
        obj = get_copy()
    for el in res:
        if el['телефон'] == str(obj['телефон']):
            print("Такой пользователь уже существует")
            return
    res.append(obj)
    with open(file, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя','фамилия','телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'
file_copy_name = 'phone_copy.csv'

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)                            
            write_file(file_name,command)
        elif command == 'r':
            if not exists(file_name):
                print("Файл не создан. Создайте его.")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_copy_name):
                create_file(file_copy_name)
            write_file(file_copy_name,command)
main()