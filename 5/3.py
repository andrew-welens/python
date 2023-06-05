minSum = int(input("Минимальная сумма инвестиций: "))
mike = int(input("Сумма у Майкла: "))
ivan = int(input("Сумма у Ивана: "))

if (mike >= minSum) and (ivan >= minSum):
    print(2)
elif mike >= minSum:
    print("Mike")
elif ivan >= minSum:
    print("Ivan")
elif mike + ivan >= minSum:
    print(1)
else:
    print(0)
