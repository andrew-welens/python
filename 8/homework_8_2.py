

userInput = int(input("Введите число: "))

arr = []

if userInput > 0:
    for i in range(userInput):
        arr.append(int(input(f"Введите число {i + 1}: ")))

lastElement = arr[-1]

arr.pop()

arr.insert(0, lastElement)

print(arr)
