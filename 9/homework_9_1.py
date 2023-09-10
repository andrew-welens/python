
n = int(input("Введите количество чисел (N): "))
numbers = input("Введите числа через пробел: ").split()

uniqueNumbers = set(numbers)

count = len(uniqueNumbers)

print("Количество различных чисел: ", count)
