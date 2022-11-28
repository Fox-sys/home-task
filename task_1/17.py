def func(a: tuple, num: int) -> tuple:
    data = list(a)
    data.append(num)
    return tuple(data)


counter = 0
tp = ()
while counter != 10:
    num = int(input())
    if num < 0 or num > 5:
        print('Введённое число не подходит, введите ещё раз')
        continue
    tp = func(tp, num)
    counter += 1

print(tp, len(set(tp)))
