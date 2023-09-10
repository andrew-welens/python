
list1 = set(input("Введите числа первого списка через пробел: ").split())
list2 = set(input("Введите числа второго списка через пробел: ").split())

commonNumbers = list1.intersection(list2)

count = len(commonNumbers)

print("Количество чисел, содержащихся одновременно в обоих списках: ", count)
