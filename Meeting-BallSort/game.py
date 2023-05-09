import random as r
import string
from time import sleep

characters = string.printable[:-6]

class Game:
    def __init__(self, colors: int, balls: int):
        self.colors = colors
        self.balls = balls
        self.tubes = [[] for _ in range(self.colors+2)]

    def generateRandomTubes(self) -> None:
        global characters
        sortedColors = [[characters[i] for _ in range(self.balls)] for i in range(self.colors)]

        for _ in range(self.balls):
            for i in range(self.colors):
                index = 0
                while True:
                    index = r.randint(0, self.colors-1)
                    if len(sortedColors[index]) > 0:
                        break

                color = sortedColors[index].pop()
                self.tubes[i].append(color)

    def makeMove(self, src:int, dest:int) -> None:
        if len(set(self.tubes[src])) < 1:
            raise Exception(f"Tube {src+1} is empty")
        if len(self.tubes[src]) == self.balls and len(set(self.tubes[src])) < 2:
            raise Exception(f"Tube {src+1} is complete, don't touch it")
        if len(self.tubes[dest]) >= self.balls:
            raise Exception(f"Tube {dest+1} is full")
        if len(self.tubes[dest]) > 0 and self.tubes[src][-1] != self.tubes[dest][-1]:
            raise Exception(f"Colors are not the same")

        color = self.tubes[src].pop()
        self.tubes[dest].append(color)


    def completed(self) -> bool:
        for tube in self.tubes:
            if 0 < len(tube) < self.balls:
                return False

            if len(set(tube)) > 1:
                return False

        return True

    def heuristic(self) -> int:
        score = 0
        for tube in self.tubes:
            score += len(set(tube))

        return score

    def __eq__(self, other) -> bool:
        for t in other.tubes:
            if t not in self.tubes:
                return False

        return True

    def __str__(self) -> str:
        output = ""
        for i, tube in enumerate(self.tubes):
            output += f"{i+1:2} ["
            for c in tube:
                output += c
            output += '\n'

        return output
