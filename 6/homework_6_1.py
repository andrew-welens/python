n = int(input("Введите число N: "))
zerosCount = 0

for i in range(n):
    num = int(input("Введите целое число: "))
    if num == 0:
        zerosCount += 1

print("Количество чисел, равных нулю:", zerosCount)
