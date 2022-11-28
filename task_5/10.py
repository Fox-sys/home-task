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
