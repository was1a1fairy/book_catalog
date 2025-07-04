import moduls
def message(text:str, type) -> str:
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

def count_books():
    """
    возвращает количество книг в каталоге
    """
    print(len(moduls.catalog_to_matrix()))

def name_catalog():
    """
    возвращает название каталога
    """
    print(moduls.open_catalog("w").name)

def date_create_catalog():
    """
    возвращает дату создания каталога
    """
    print("04.07.2025")

def print_catalog():
    """"
    вывод каталога на консоль
    """
    for i in (moduls.catalog_to_matrix()):
        print(*i)

def input_book():
    """
    добавление полной информации о книге в каталог
    """
    name = message("введите название книги одной строкой", str)
    author = message("введите автора данной книги одной строкой", str)
    year = message("введите год издания данной книги целым числом", int)
    genre = message("введите жанр данной книги одной строкой", str)
    count = message("введите  количество экземпляров этой книги, имеющихся в наличии, целым числом", int)
    moduls.open_catalog("w").write(name, author, year, genre, count)
    report("книга добавлена успешно!")