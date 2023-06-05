def hasVowels(word):
    vowels = "aeiou"
    vowelCount = 0
    consonantCount = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for letter in word:
        if letter.isalpha():
            if letter in vowels:
                vowelCount += 1
                print(letter)
                if (letter == "a"):
                    a += 1
                if (letter == "e"):
                    e += 1
                if (letter == "i"):
                    i += 1
                if (letter == "o"):
                    o += 1
                if (letter == "u"):
                    u += 1
            else:
                consonantCount += 1

    if vowelCount > 0:
        print("Количество гласных букв:", vowelCount)
        print("Количество согласных букв:", consonantCount)
        if (a >= 1):
            print(f"Количество a = {a}")
        if (e >= 1):
            print(f"Количество e = {e}")
        if (i >= 1):
            print(f"Количество i = {i}")
        if (o >= 1):
            print(f"Количество o = {o}")
        if (u >= 1):
            print(f"Количество u = {u}")
    else:
        print("False")


word = input("Введите слово: ")

hasVowels(word)
