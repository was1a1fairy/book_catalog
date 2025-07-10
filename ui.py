import moduls
import os
import time

def message(text:str, typee):

    """
    при вызове функции в параметры передаем text,
    с сообщением для пользователя

    на выходе получаем данные от пользователя
    """

    mess = input(f"{text},\nесли вы не знаете, введите 'no' \033[1;32m->\033[0m ")

    if mess != "no":
        mess = moduls.check_input(mess, typee)

    return mess


def report(text: str):

    """
    возвращает пользователю сообщение на консоль
    """

    print(f"\033[4m{text}\033[0m")


def count_books(path: str) -> int:

    """
    возвращает количество книг в каталоге
    """

    return len(moduls.catalog_to_array(path))


def name_catalog(path: str) -> str:

    """
    возвращает название каталога
    """

    return moduls.open_catalog(path, "w").name


def date_create_catalog(path) -> str:

    """
    возвращает дату создания каталога
    """
    return time.ctime(os.path.getctime(path))


def print_array(array: list, path: str):

    if moduls.is_empty(path):
        report("каталог пуст, сначала добавьте книги")
        return

    print(*array)


def menu() -> str:

    """
    основное меню, которое будет видеть пользователь
    """

    mess = message(f"\033[1;32mНажмите:\033[0m\n"
            f"\033[1;32m1\033[0m - если хотите создать каталог(или очистить его)\n"
            f"\033[1;32m2\033[0m - если хотите добавить книгу и информацию о ней\n"
            f"\033[1;32m3\033[0m - если хотите прочитать каталог\n"
            f"\033[1;32m4\033[0m - если хотите удалить книгу из каталога\n"
            f"\033[1;32m5\033[0m - если хотите редактировать информацию о книге\n"
            f"\033[1;32m6\033[0m - если хотите посмотреть информацию о каталоге\n"
            f"\033[1;32mno\033[0m - если хотите выйти и завершить работу приложения", int)

    if mess == "no":
        report("совершен выход из приложения")
        exit()

    return mess


def core(path):

    """
    сценарий
    """

    mess = menu()

    if mess == 1:
        moduls.open_catalog(path, "w")
        report("каталог создан!")

    elif mess == 2:
        moduls.input_book(path)

    elif mess == 3:
        print_array(moduls.catalog_to_array(path), path)

    elif mess == 4:
        moduls.delete_book(path)

    elif mess == 5:
        moduls.modify_book(path)

    elif mess == 6:
        count = count_books(path)
        data = date_create_catalog(path)
        name = name_catalog(path)
        report(f"\033[1;32mИнформация о каталоге:\033[0m\n"
               f"Дата создания: {data},\n"
               f"Количество книг: {count},\n"
               f"Имя каталога: {name}.")

    else: raise ValueError("команда должна быть от 1 до 6, либо no")