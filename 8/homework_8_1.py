
userInput = int(input("Введите число: "))

arr = []

for i in range(userInput):
    arr.append(int(input(f"Введите число {i + 1}: ")))

reversArr = arr[::-1]

print("result", reversArr)
