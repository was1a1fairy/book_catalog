import ui


def check_input(data, typee):

    """
    проверка типа входных данных,
    если число, то больше 0,
    перевод в int
    """
    if data.isdigit():
        data = int(data)
        print(data)

    if not isinstance(data, typee): raise TypeError("введите правильный тип данных")

    if typee in (int, float):
        if data<=0: raise ValueError("число должно быть больше 0")
    return data

def catalog_to_matrix(path):

    """
    перевод информации из файла в матрицу
    """

    file = open_catalog(path, "r")
    matrix = []

    for string in file.readlines():
        matrix.append(string.split(","))

    return matrix


def open_catalog(path, mode: str):

    """
    открытие файла в указанном в параметрах функции режиме
    """

    file = open(path, mode)
    return file


def is_empty(path) -> bool:

    if open_catalog(path, "r").read() == "":
        return True

    return False


def input_book(path):

    """
    добавление полной информации о книге в каталог
    """

    name = ui.message("введите название книги одной строкой", str)
    author = ui.message("введите автора данной книги одной строкой", str)
    year = ui.message("введите год издания данной книги целым числом", int)
    genre = ui.message("введите жанр данной книги одной строкой", str)
    count = ui.message("введите  количество экземпляров этой книги, имеющихся в наличии, целым числом", int)
    string = f"{name}, {author}, {year}, {genre}, {count}"
    open_catalog(path, "a").write(string)
    ui.report("книга добавлена успешно!")


def delete_book(path):

    """
    удаление книги из матрицы,
    затем матрицу заново в файл
    если clear не сработает
    перебрать каталог через i и j
    и удалить всё по индексам.
    """

    if is_empty(path):
        ui.report("каталог пуст, сначала добавьте книги")
        return

    book = ui.message("введите название книги, которую хотите удалить из каталога", str)
    catalog = catalog_to_matrix(path)

    for string in catalog:
        if book in string:
            string.clear()

    open_catalog(path, "w").write(catalog)
    ui.report("книги больше нет в каталоге! или не было)))!")


def modify_book(path):

    """
    замена инфы о книге
    """

    if is_empty(path):
        ui.report("каталог пуст, сначала добавьте книги")
        return

    book = ui.message("введите название книги, которую хотите изменить", str)
    note = choose_note(path, book)
    catalog = catalog_to_matrix(path)

    for string in catalog:
        if book in string:
            string[note] = ui.message("введите выбранные вами данные для изменения",
                                   [int if note==3 or note==5 else str])

    ui.report("информация о книге успешно изменена")


def choose_note(path, book):

    """
    для функции modify_book
    пользователь выбирает какую инфу о книге хочет заменить,
    если пользователь передумал и ввел "-", выход.
    """

    catalog = catalog_to_matrix(path)

    for string in catalog:
        if book in string:
            note = ui.message(f"название: {book}. Если хотите его изменить, нажмите 1\n"
                    f"автор: {string[2]}. Если хотите изменить, нажмите 2\n"
                    f"год издания: {string[3]}. Если хотите изменить, нажмите 3\n"
                    f"жанр: {string[4]}. Если хотите изменить, нажмите 4\n"
                    f"количество книг в наличии: {string[5]}. Если хотите изменить, нажмите 5", int)

            if note >= 1 and note <= 5:
                return note

            elif note == "-":
                ui.report("изменения не произошли")
                return

            raise ValueError("введите значение от 1 до 5!")

    ui.report("неправильное название/книги нет в каталоге")