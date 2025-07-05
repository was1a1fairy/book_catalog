import moduls

def message(text:str, type):
    """
    при вызове функции в параметры передаем text,
    с сообщением для пользователя

    на выходе получаем данные от пользователя
    """
    message = input(f"{text}, если вы не знаете, введите '-'")
    if message!="-":
        moduls.check_input(message, type)
    else:
        message = "неизвестно"
    return message

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