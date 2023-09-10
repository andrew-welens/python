

fishermanCount = int(input("Количество рыбаков: "))
fishermanWeight = []
maxBoatCapability = int(input("Максимальная нагрузка в лодке: "))
boatCount = 0
fishermanWhoCant = 0

if fishermanCount > 0:
    for i in range(fishermanCount):
        fishermanWeight.append(int(input(f"Введите вес {i + 1} рыбака: ")))

    fishermanWeight.sort()

    left = 0
    right = fishermanCount - 1

    while left <= right:
        if fishermanWeight[left] + fishermanWeight[right] <= maxBoatCapability:
            left += 1
            right -= 1
        else:
            right -= 1
        boatCount += 1

print(f"Необходимо {boatCount} лодки, чтобы переправить {fishermanCount} путешественников")
