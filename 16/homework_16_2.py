
class Turtle:
    def __init__(self, x, y, s, x2, y2):
        self.x = x
        self.y = y
        self.s = s
        self.x2 = x2
        self.y2 = y2

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1

    def count_moves(self):
        countX = abs(self.x2 - self.x) / self.s
        countY = abs(self.y2 - self.y) / self.s
        countXY = countX + countY
        print(
            f'Минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции = {countXY}')


turtle = Turtle(1, 1, 1, 50, 30)

command = 0

while command != 69:
    print("Enter action:")
    print("1. up")
    print("2. down")
    print("3. left")
    print("4. right")
    print("5. evolve")
    print("6. degrade")
    print("7. count moves")
    print("69. stop")
    command = int(input())

    if command == 1:
        turtle.go_up()
    elif command == 2:
        turtle.go_down()
    elif command == 3:
        turtle.go_left()
    elif command == 4:
        turtle.go_right()
    elif command == 5:
        turtle.evolve()
    elif command == 6:
        turtle.degrade()
    elif command == 7:
        turtle.count_moves()
    elif command == 69:
        print("Goodbye, see you later!")
    else:
        print("Invalid action, enter action from menu")
