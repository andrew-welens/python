a = map(int, input("Введите пятизначное число: "))

data = list(a)

if len(data) == 5:
    result = ((data[3] ** data[4]) * data[2]) / (data[0] - data[1])
    print(result)
else:
    print('Ошибка, введите пятизначное число')
