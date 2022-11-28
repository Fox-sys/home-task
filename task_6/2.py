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
