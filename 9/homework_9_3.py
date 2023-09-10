
numbers = input("Введите последовательность чисел через пробел: ").split()
seenNumbers = set()

for number in numbers:
    if number in seenNumbers:
        print("YES")
    else:
        print("NO")
        seenNumbers.add(number)
