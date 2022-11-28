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


if __name__ == '__main__':
    main()
