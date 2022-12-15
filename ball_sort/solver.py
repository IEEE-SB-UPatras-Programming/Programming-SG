from copy import deepcopy
from game import *
from typing import Any, Union
from queue import PriorityQueue

class Node:
    def __init__(self, parent: Any, game: Game, move: tuple[int, int]):
        self.parent = parent
        self.game = game
        self.cost = (parent.cost + 1) if parent is not None else 0
        self.score = game.heuristic()
        self.move = move

    def getChildren(self) -> list:
        children = []

        for i in range(self.game.colors+2):
            for j in range(self.game.colors+2):
                if i == j: continue
                if j == self.move[0] and i == self.move[1]: continue

                try:
                    nextGame = deepcopy(self.game)
                    nextGame.makeMove(i, j)
                    child = Node(self, nextGame, (i, j))
                    children.append(child)
                except Exception:
                    pass

        return children

    def __eq__(self, other):
        return (self.cost+self.score) == (other.cost+other.score)

    def __lt__(self, other):
        return (self.cost+self.score) < (other.cost+other.score)

    def __gt__(self, other):
        return (self.cost+self.score) > (other.cost+other.score)

def badsolve(game: Game) -> Union[list, None]:
    openList = PriorityQueue()
    openList.put(Node(None, game, (0,0)))
    closedList = []

    while not openList.empty():
        currentNode = openList.get()

        if currentNode.game.completed():
            path = []
            while currentNode.parent is not None:
                path.append(currentNode.move)
                currentNode = currentNode.parent
            return path

        if currentNode not in closedList:
            closedList.append(currentNode)

        children = currentNode.getChildren()
        for child in children:
            openList.put(child)

    return None

def goodsolve(game: Game, visitedPositions=[]) -> Union[list, None]:
    visitedPositions.append(game)

    for i in range(game.colors+2):
        for j in range(game.colors+2):
            if i == j: continue

            nextGame = deepcopy(game)
            try:
                nextGame.makeMove(i, j)
            except Exception:
                continue

            if nextGame.completed():
                return [(i, j)]

            if nextGame not in visitedPositions:
                result = goodsolve(nextGame, visitedPositions)
                if result is not None:
                    result.append((i, j))
                    return result

    return None
