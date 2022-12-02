import os
from enum import IntEnum


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    WIN = 6
    LOSS = 0
    DRAW = 3


def mapCodeToShape(code: str) -> Shape:
    if code in ["A", "X"]:
        return Shape.ROCK
    if code in ["B", "Y"]:
        return Shape.PAPER
    if code in ["C", "Z"]:
        return Shape.SCISSORS
    raise Exception("Invalid shape code")


def playGame(myShape: Shape, opponentShape: Shape) -> Outcome:
    if myShape == opponentShape:
        return Outcome.DRAW

    if myShape == Shape.ROCK:
        return Outcome.WIN if opponentShape == Shape.SCISSORS else Outcome.LOSS
    if myShape == Shape.PAPER:
        return Outcome.WIN if opponentShape == Shape.ROCK else Outcome.LOSS
    if myShape == Shape.SCISSORS:
        return Outcome.WIN if opponentShape == Shape.PAPER else Outcome.LOSS

    raise Exception("Unexpected play")


print(os.path.dirname(__file__))
with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    games = inputFile.read().splitlines()
    totalGameScore = 0
    for game in games:
        opponentShapeCode, myShapeCode = game.split(" ")
        myShape = mapCodeToShape(myShapeCode)
        opponentShape = mapCodeToShape(opponentShapeCode)
        gameResult = playGame(myShape, opponentShape)
        gameScore = myShape.value + gameResult.value

        totalGameScore += gameScore

    print(f"My total score would be {totalGameScore}")
