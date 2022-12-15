import os
from game import *
from solver import goodsolve, badsolve

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getColors() -> int:
    colors = 0
    while True:
        print("Number of colors: ", end="")
        colors = int(input())
        if colors > len(characters):
            print("Whoa hold your horses, we don't have that many colors")
        elif colors < 2:
            print("Buddy you gotta have at least two colors")
        else:
            return colors

def getBalls() -> int:
    balls = 0
    while True:
        print("Number of balls: ", end="")
        balls = int(input())
        if balls > 80:
            print("Jesus H Christ, that's way too many balls")
        elif balls < 2:
            print("Buddy you gotta have at least two balls")
        else:
            return balls

def getMode() -> bool:
    print("Choose game mode [manual/auto]: ", end="")
    mode = ""
    while True:
        mode = input()
        if mode in ["manual", "auto"]:
            return True if mode=="manual" else False

        print("Please choose valid option")


def getMove(colors) -> tuple[int, int]:
    src = dest = 0

    while True:
        print("Source: ", end='')
        src = int(input())
        if src == -1:
            return src, 0
        elif src in range(1,colors+3):
            break

        print("Source out of range")

    while True:
        print("Destination: ", end='')
        dest = int(input())

        if dest in range(1,colors+3):
            break

        print("Destination out of range")

    return src-1, dest-1

def main():
    clear()
    colors = getColors()
    balls = getBalls()

    game = Game(colors, balls)
    game.generateRandomTubes()

    clear()
    print(game)

    mode = getMode()

    if mode:
        while True:
            clear()
            print(game)

            if game.completed():
                print("Congratulations you solved it")
                break

            src, dest = getMove(colors)
            if src == -1:
                break

            try:
                game.makeMove(src, dest)

            except Exception as e:
                print(e)
                sleep(2)
    else:
        clear()
        print(game)

        result = goodsolve(game)
        if result == None:
            print("This game somehow cannot be solved")
            return

        result.reverse()
        for move in result:
            print(f"{move[0]+1} -> {move[1]+1}")
            game.makeMove(move[0], move[1])
            print(game)

if __name__ == "__main__":
    main()
