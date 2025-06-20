def message(text:str) -> str:
    """
    при вызове функции в параметры передаем text,
    с сообщением для пользователя

    на выходе получаем данные от пользователя
    """
    message = input(text)
    return message

def report(text: str):
    """
    возвращает пользователю сообщение на консоль
    """
    print(text)