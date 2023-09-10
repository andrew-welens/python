numA = int(input("Введите число A: "))
numB = int(input("Введите число B: "))
oddNumbers = 0

for i in range(numA, numB + 1):
    if (i % 2 == 0) and not (i == 0):
        print(i)
        oddNumbers += 1
print("Количество четных чисел: ", oddNumbers)
