import moduls

def message(text:str, typee):
    """
    при вызове функции в параметры передаем text,
    с сообщением для пользователя

    на выходе получаем данные от пользователя
    """
    mess = input(f"{text}, если вы не знаете, введите '-'")
    if mess != "-":
        mess = moduls.check_input(mess, typee)
        print(mess)
    else:
        mess = "неизвестно"
    return mess

def report(text: str):
    """
    возвращает пользователю сообщение на консоль
    """
    print(text)

def count_books(path):
    """
    возвращает количество книг в каталоге
    """
    print(len(moduls.catalog_to_matrix(path)))

def name_catalog(path):
    """
    возвращает название каталога
    """
    print(moduls.open_catalog(path, "w").name)

def date_create_catalog():
    """
    возвращает дату создания каталога
    """
    print("04.07.2025")

def print_catalog(path):
    """"
    вывод каталога на консоль
    """
    for i in (moduls.catalog_to_matrix(path)):
        print(*i)

def menu():
    """
    основное меню, которое будет видеть пользователь
    """
    mess = message(f"Нажмите:\n"
            f"1 - если хотите создать каталог\n"
            f"2 - если хотите добавить книгу и информацию о ней\n"
            f"3 - если хотите прочитать каталог\n"
            f"4 - если хотите удалить книгу из каталога\n"
            f"5 - если хотите редактировать информацию о книге\n"
            f"6 - если хотите посмотреть информацию о каталоге\n"
            f"- - если хотите выйти и завершить работу приложения", int)
    if mess == "-":
        report("совершен выход из приложения")
        exit()
    return mess