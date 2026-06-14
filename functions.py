def fill_int(what, maxbord, minbord):
    while True:
        try:
            num = int(input(f"Введите {what}"))
        except ValueError:
            print("Нужно ввести число")
            continue
        if num > maxbord:
            print("Число слишком большое")
            continue
        if num < minbord:
            print("Число недопустимое")
            continue
        else:
            break
    return num