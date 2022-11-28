try:
    a = int(input()) + 1
except ValueError:
    print('Это должно быть число')
    raise SystemExit

for i in range(1, a):
    for j in range(1, i+1):
        print(j, end='')
    print()
for i in range(a-1, 1, -1):
    for j in range(1, i):
        print(j, end='')
    print()