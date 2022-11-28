LETTERS = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(1072, 1104)]


def main(ln: int) -> dict:
    dc = {}
    for i in range(ln):
        try:
            key = int(input('Введите ключ: '))
        except ValueError:
            print('Ключ это число, значение пропущено')
            continue
        value = input('Введите имя: ')
        error = False
        for letter in value.lower():
            if letter not in LETTERS:
                error = True
                print('Значение должно состоять только из букв')
                break
        if error:
            continue
        dc[key] = value
    return dc


try:
    ln = int(input('Введите длинну словаря: '))
except ValueError:
    print('Вводить надо число')
    raise SystemExit


print(main(ln))
