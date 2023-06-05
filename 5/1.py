userInt = int(input("Введите целое число: "))
if userInt == 0:
    print("Ноль")
elif userInt % 2 == 0:
    if userInt > 0:
        print("Положительное четное число")
    else:
        print("Отрицательное четное число")
elif userInt % 2 == 1:
    if userInt > 0:
        print("Положительное нечётное число")
    else:
        print("Отрицательное нечётное число")
