import math


class CashRegister:
    def __init__(self, cash):
        self.cash = cash

    def showAllCache(self):
        print(self.cash)

    def topUp(self, cash):
        if cash > 0:
            self.cash += cash

    def count1000(self):
        if self.cash >= 1000:
            count = math.floor(self.cash / 1000)
        print(f'Целых тысяч в кассе: {count}')

    def takeAway(self, cash):
        if self.cash >= cash:
            self.cash -= cash
        else:
            print('Не достаточно денег в кассе')


cashReg = CashRegister(10000)

command = 0

while command != 5:
    print('Menu:')
    print('1. Top up')
    print('2. Count 1000')
    print('3. Take away')
    print('4. Show all cash')
    print('5. Close cash register')
    command = int(input('Enter number from menu: '))
    if command == 1:
        summ = int(input('Enter a summ, that you want to top up: '))
        cashReg.topUp(summ)
    if command == 2:
        cashReg.count1000()
    if command == 3:
        summ = int(input('Enter a summ, that you want to take away: '))
        cashReg.takeAway(summ)
    if command == 4:
        cashReg.showAllCache()
    if command == 5:
        print('Goodbye, see you later!')
    else:
        print('Enter command number from menu')
