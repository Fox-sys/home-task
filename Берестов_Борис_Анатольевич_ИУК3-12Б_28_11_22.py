def task_1_10():
    """
        Напишите функцию которая принимает список длина списка должна , ,
        быть произвольной Получите из этого списка кортеж и верните его .
        элементы с в обратном порядке Показать на примере
    """
    def func(a: list) -> tuple:
        return tuple(a[::-1])

    print(func([1, 2, 3, 4]))


def task_1_17():
    """
        Создайте функцию которая заполнит один кортеж десятью случайными ,
        целыми числами от до включительно через циклический ввод по 0 5 (
        input() int(), ). и проверять введенное число на соблюдение условия
        Определите число уникальных элементов кортежа и верните его из
        функции Показать на примере
    """
    def func(a: tuple, num: int) -> tuple:
        data = list(a)
        data.append(num)
        return tuple(data)

    counter = 0
    tp = ()
    while counter != 10:
        try:
            num = int(input())
            if num < 0 or num > 5:
                raise ValueError
        except ValueError:
            print('Введённое число не подходит, введите ещё раз')
            continue
        tp = func(tp, num)
        counter += 1

    print(tp, len(set(tp)))


def task_2_11():
    """
        Напишите функцию которая принимает список создать его заранее , (
        через циклический ввод по длина списка должна быть input(),
        произвольной т е определить условие конца ввод и меняет местами его , . . )
        первый и последний элемент В исходном списке минимум элемента . 2
        ( ). . проверять возвращаем из функции новый список Показать на примере
    """
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


def task_2_23():
    """
        Напишите функцию которая создает х мерный список через , 2
        циклический ввод по число строк и столбцов списка должна быть input(),
        произвольной вводим эти числа через На выходе вернуть ( int(input())).
        список из этих элементов и посчитать и вывести сумму элементов по ( )
        строкам.
    """
    def func(a: int, b: int) -> tuple[list[list], list]:
        try:
            ls = [[int(input('Введите число, не букву: ')) for i in range(b)] for j in range(a)]
        except ValueError:
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


def task_3_2():
    """
        Напишите функцию которая будет выводить ключ по значению должна , (
        производить поиск по значению и выдавать ключ ).
        Подставьте Входные данные в свою программу и сравните результат с " "
        выходными данными .
        1) : {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}; Входные данные Параметр для
        input() : 'Hi'. : 'Hello'. 2) : {'beep' : 'car'}; Выходные данные Входные данные
        Параметр для Выходные данные Входные данные input() : 'car'. : 'beep'. 3) : {'a' :
        1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}; input() : 5. : 'e'.
    """
    DATA = {
        "Hello": "Hi",
        "Bye": "Goodbye",
        "List": "Array"
    }

    def search(word: str) -> str:
        for k, v in DATA.items():
            if v == word:
                return k

    while (a := input()) != 'exit':
        print(search(a))


def task_3_20():
    """
        Разработайте функцию которая создает словарь из ввода числа и строки ,
        ( , ). например номер по журналу и имя Вводим данные через циклический
        ввод по длина словаря должна быть произвольной проверяем input(), ,
        данные на корректность е должно быть только цифры второе только (1- ,
        буквы и не добавляем если правила не выполнены Вернуть словарь ) , . .
        Показать на примере
    """
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


def task_4_1():
    """
        По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я
        ступенька состоит из чисел от 1 до i без пробелов.
        1) : 1. : 1 Входные данные Выходные данные
        2) : 3. : Входные данные Выходные данные
        1
        12
        123
        3) : 5. : Входные данные Выходные данные
        1
        12
        123
        1234
        12345
    """
    try:
        a = int(input()) + 1
    except ValueError:
        print('Это должно быть число')
        raise SystemExit

    for i in range(1, a):
        for j in range(1, i + 1):
            print(j, end='')
        print()


def task_4_5():
    """
        Используя циклы напишите код который бы выводил данную фигуру , , :
         1
         21
         321
         4321
         54321
         654321
         7654321
         87654321
         987654321
         87654321
         7654321
         654321
         54321
         4321
         321
         21
         1
        Программа должна выводить фигуру разной величины в зависимости от ,
        входного параметра Значение параметра может принимать значения от .
        0 9.
    """
    try:
        a = int(input()) + 1
    except ValueError:
        print('Это должно быть число')
        raise SystemExit

    for i in range(1, a):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    for i in range(a - 1, 1, -1):
        for j in range(1, i):
            print(j, end='')
        print()


def task_5_3():
    """
        Даны два множества чисел Напишите функцию которая определяет . , ,
        является ли первое множество подмножеством второго Множество .
        является подмножеством другого множества если все данные первого ,
        совпадают с частью данных из второго Если множества совпадают они . ,
        не являются подмножествами друг друга .
        Подставьте Входные данные в свою программу и сравните результат с " "
        выходными данными Входные данные Выходные . 1) : {1, 2, 3} {1, 4, 5}.
        значения Входные данные : False. 2) : {1, 2, 3, 4, 5, 6, 7} {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}.
        Выходные значения Входные данные : True. 3) : {1, 10, 223, 413, 2} {1, 10, 223,
        413, 2}. : False.
    """
    def check_sub_set(a: set, b: set) -> bool:
        return a < b

    while True:
        try:
            a = set(map(int, input('Введите числа через пробелл: ').split(' ')))
            b = set(map(int, input('Введите числа через пробелл: ').split(' ')))
            print(check_sub_set(a, b) or check_sub_set(b, a))
        except ValueError:
            print('Надо было вводить числа')


def task_5_10():
    """
        Функция сздает список элементов через циклический ввод по input(),
        длина списка должна быть произвольной а элементами могут быть ,
        символы алфавита только буквы или цифры от до проверять ( ) 0 9 (
        корректность вводимых объектов и не добавлять в список при нарушении
        правила Преобразуйте его в множество Верните множество и его ). .
        мощность Показать на примере
    """
    LETTERS = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(48, 58)]

    def check_set(a: set) -> int:
        return len(a)

    st = set()
    while (a := input()) != '/exit':
        has_error = False
        for i in a:
            if i not in LETTERS:
                print('Значение не заносится, есть недопустимые символы')
                has_error = True
                break
        if has_error:
            continue
        st.add(a)

    print(check_set(st))

    check_set({1, 2})  # 2
    check_set({1, 2, 'hz'})  # 3


def task_6_1():
    """
        присутствовать следующие поля имя студента возраст оценка за : , ,
        семестр город проживания В цикле берем каждый элемент кортежа и , .
        обеспечиваем вычисление средней оценки по всем учащимся Выводить : .
        на печать следующе Ученики список имен студентов через запятую в : “ { }
        этом семестре хорошо учатся В список студентов которые выводятся по !”. ,
        результатам работы попадут лишь те у которых оценка за семестр равна , ,
        или выше средней по всем учащимся .
    """
    NAME = 'name'
    AGE = 'age'
    MARK = 'mark'
    CITY = 'city'

    def student_init(name: str, age: int, mark: float, city: str) -> dict:
        return {NAME: name, AGE: age, MARK: mark, CITY: city}

    def check_mark(student: dict, middle_mark: float) -> bool:
        return student[MARK] > middle_mark

    def init() -> tuple:
        return (
            student_init('Timmy', 18, 3.47, 'town1'),
            student_init('Oleg', 19, 4.15, 'town2'),
            student_init('Kirill', 18, 2.5, 'town3'),
            student_init('IDK', 20, 5, 'town2'),
            student_init('God knows', 18, 4.8, 'town3'),
            student_init('It\'s to difficult to think up names', 18, 2, 'town4'),
            student_init('Timmy 2', 18, -1, 'town1'),
        )

    def count_middle_mark(students: tuple[dict]) -> float:
        return round(sum([i[MARK] for i in students]) / len(students), 2)

    def main():
        students = init()
        middle_mark = count_middle_mark(students)
        good_students = []
        bad_students = []
        for student in students:
            if check_mark(student, middle_mark):
                good_students.append(student)
            else:
                bad_students.append(student)
        print('Хорошие студенты: ', end='')
        for student in good_students:
            print(student[NAME], end=', ')
        print()
        print('Плохие студенты: ', end='')
        for student in bad_students:
            print(student[NAME], end=', ')

    main()


def task_6_2():
    """
        Дана строка в виде случайной последовательности чисел от до вводим 0 9 (
        через например как input(), '112342341234569').
        Требуется создать словарь который в качестве ключей будет принимать ,
        данные числа т е ключи будут типом а в качестве значений ( . . int), –
        количество этих чисел в имеющейся последовательности
    """
    LETTERS = [chr(i) for i in range(48, 58)]

    def count_nums(a: str) -> dict:
        counter = {}
        for i in set(a):
            counter[i] = a.count(i)
        return counter

    def check_str(a: str) -> bool:
        has_error = False
        for i in a:
            if i not in LETTERS:
                has_error = True
                break
        return has_error

    a = input()
    if check_str(a):
        raise SystemExit

    print(count_nums(a))


TASKS = [
    [task_1_10, task_1_17],
    [task_2_11, task_2_23],
    [task_3_2, task_3_20],
    [task_4_1, task_4_5],
    [task_5_3, task_5_10],
    [task_6_1, task_6_2]
]

while True:
    print()
    a = int(input('Выберете блок: ')) - 1
    b = int(input('Выберете задание: ')) - 1
    try:
        TASKS[a][b]()
    except SystemExit:
        pass
