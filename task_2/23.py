def func(a: int, b: int) -> tuple[list[list], list]:
    try:
        ls = [[int(input('Введите число, не букву: ')) for i in range(b)] for j in range(a)]
    except:
        print('Вводить надо числа')
        raise SystemExit
    sum_list = []
    for item in ls:
        sum_list.append(sum(item))
    return ls, sum_list



try:
    a = int(input())
    b = int(input())
    print(func(a, b))
except Exception as e:
    print(e)