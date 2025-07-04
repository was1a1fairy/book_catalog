import moduls
def message(text:str, type) -> str:
    """
    при вызове функции в параметры передаем text,
    с сообщением для пользователя

    на выходе получаем данные от пользователя
    """
    message = input(text)
    moduls.check_input(message, type)
    return message

def report(text: str):
    """
    возвращает пользователю сообщение на консоль
    """
    print(text)

def count_books():
    """
    возвращает количество книг в каталоге
    """
    return len(moduls.catalog_to_matrix())

def name_catalog():
    """
    возвращает название каталога
    """
    return "book_catalog"

def date_create_catalog():
    """
    возвращает дату создания каталога
    """
    return "04.07.2025"