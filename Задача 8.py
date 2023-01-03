x, y = int(input()), int(input())
if x == 0 and y == 0:
    print('Некорректные данные!')
elif x == 0:
    print('OY')
elif y == 0:
    print('OX')
elif x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)                        