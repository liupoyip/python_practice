n = 5

for i in range(5):
    level = i*2 + 1
    for _ in range(level):
        print('*', end='')
    print()
