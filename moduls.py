def check_input(data, type):
    if not isinstance(data, type): raise TypeError("введите правильный тип данных")
    if isinstance(type, (int, float)):
        if data<=0 or data>=2025: raise ValueError("число должно быть валидным")
