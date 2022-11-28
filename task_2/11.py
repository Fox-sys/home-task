def func(a: list) -> list:
    a[0], a[-1] = a[-1], a[0]
    return a


ls = []
while True:
    a = input()
    if a == 'exit' and len(ls) > 1:
        break
    elif len(ls) < 2 and a == 'exit':
        print('Введите ещё хотябы один элемент')
        continue
    ls.append(a)


print(func(ls))
