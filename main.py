import sys

playerX = "\033[91m{}\033[00m".format("X")
playerO = "\033[96m{}\033[00m".format("O")


def printField(f):
    print("┎" + ("---┬" * 2) + "---┒")
    i = 0
    for row in f:
        p = ""
        for column in row:
            p += "│ " + column + " "
        p += "│"
        print(p)
        if i < 2:
            print("├" + ("---┼" * 2) + "---┤")
        i += 1

    print("┖" + ("---┴" * 2) + "---┚")
    print()


thisPlayer = playerX


def getInput(f):
    print("Spieler " + thisPlayer + " ist am zug:")

    x = int(input("  pos x: ")) - 1
    y = int(input("  pos y: ")) - 1

    if f[y][x] == " ":
        f[y][x] = thisPlayer
    else:
        print("\n" * 100)
        printField(f)
        print("Field already used!!!")
        f = getInput(f)

    return f


def controlField():
    end = False
    if field[0][0] == thisPlayer and field[0][0] == field[0][1] and field[0][1] == field[0][2] or \
            field[1][0] == thisPlayer and field[1][0] == field[1][1] and field[1][1] == field[1][2] or \
            field[2][0] == thisPlayer and field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        end = True

    elif field[0][0] == thisPlayer and field[0][0] == field[1][0] and field[1][0] == field[2][0] or \
            field[0][1] == thisPlayer and field[0][1] == field[1][1] and field[1][1] == field[2][1] or \
            field[0][2] == thisPlayer and field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        end = True

    elif field[0][0] == thisPlayer and field[0][0] == field[1][1] and field[1][1] == field[2][2] or \
            field[0][2] == thisPlayer and field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        end = True

    elif field[0][0] != " " and field[0][1] != " " and field[0][2] != " " and \
            field[1][0] != " " and field[1][1] != " " and field[1][2] != " " and \
            field[2][0] != " " and field[2][1] != " " and field[2][2] != " ":
        print("\n" * 100)
        print("Its a Tie!!")
        sys.exit()

    if end:
        print("\n" * 100)
        print("Player " + thisPlayer + " won!!")
        sys.exit()


field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

print("\n" * 100)

while True:
    printField(field)
    field = getInput(field)
    controlField()
    if thisPlayer == playerX:
        thisPlayer = playerO
    else:
        thisPlayer = playerX

    print("\n" * 100)
