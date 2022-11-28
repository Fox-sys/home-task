def check_sub_set(a: set, b: set) -> bool:
    return a < b


while True:
    try:
        a = set(map(int, input('Введите числа через пробелл: ').split(' ')))
        b = set(map(int, input('Введите числа через пробелл: ').split(' ')))
        print(check_sub_set(a, b) or check_sub_set(b, a))
    except ValueError:
        print('Надо было вводить числа')