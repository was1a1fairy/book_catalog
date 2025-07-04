def check_input(data, type):
    """
    проверка типа входных данных,
    если число, то больше 0
    """
    if not isinstance(data, type): raise TypeError("введите правильный тип данных")
    if isinstance(type, (int, float)):
        if data<=0: raise ValueError("число должно быть больше 0")

def catalog_to_matrix():
    """
    перевод информации из файла в матрицу
    """
    file = open("book_catalog.txt", "r")
    matrix = []
    for string in file.readlines():
        matrix.append(string.split(","))
    return matrix

def open_catalog(mode: str):
    """
    открытие файла в указанном в параметрах функции режиме
    """
    file = open("book_catalog.txt", mode)
    return file