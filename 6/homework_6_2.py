x = int(input("Введите натуральное число X: "))
divisorsCount = 0

for i in range(1, x + 1):
    if x % i == 0:
        divisorsCount += 1

print("Количество натуральных делителей числа X:", divisorsCount)
