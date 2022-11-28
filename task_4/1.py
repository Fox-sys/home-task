try:
    a = int(input()) + 1
except ValueError:
    print('Это должно быть число')
    raise SystemExit

for i in range(1, a):
    for j in range(1, i+1):
        print(j, end='')
    print()