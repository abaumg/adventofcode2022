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


def mapCodeToShapePart1(code: str) -> Shape:
    if code in ["A", "X"]:
        return Shape.ROCK
    if code in ["B", "Y"]:
        return Shape.PAPER
    if code in ["C", "Z"]:
        return Shape.SCISSORS
    raise Exception("Invalid shape code")


def mapCodeToShapePart2(code: str) -> Shape:
    if code == "A":
        return Shape.ROCK
    if code == "B":
        return Shape.PAPER
    if code == "C":
        return Shape.SCISSORS
    raise Exception("Invalid shape code")


def mapCodeToOutcome(code: str) -> Outcome:
    if code == "X":
        return Outcome.LOSS
    if code == "Y":
        return Outcome.DRAW
    if code == "Z":
        return Outcome.WIN
    raise Exception("Invalid outcome code")


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


def calculateRequiredShape(opponentShape: Shape, desiredOutcome: Outcome) -> Shape:
    if desiredOutcome == Outcome.DRAW:
        return opponentShape

    if opponentShape == Shape.ROCK:
        return Shape.PAPER if desiredOutcome == Outcome.WIN else Shape.SCISSORS
    if opponentShape == Shape.PAPER:
        return Shape.SCISSORS if desiredOutcome == Outcome.WIN else Shape.ROCK
    if opponentShape == Shape.SCISSORS:
        return Shape.ROCK if desiredOutcome == Outcome.WIN else Shape.PAPER

    raise Exception("Unexpected result")


with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    games = inputFile.read().splitlines()
    solutionPart1 = 0
    solutionPart2 = 0
    for game in games:
        opponentShapeCode, myShapeCode = game.split(" ")
        expectedOutcomeCode = myShapeCode

        myShapePart1 = mapCodeToShapePart1(myShapeCode)
        opponentShapePart1 = mapCodeToShapePart1(opponentShapeCode)
        gameResultPart1 = playGame(myShapePart1, opponentShapePart1)
        gameScorePart1 = myShapePart1.value + gameResultPart1.value

        expectedOutcome = mapCodeToOutcome(expectedOutcomeCode)
        opponentShape = mapCodeToShapePart2(opponentShapeCode)
        myShapePart2 = calculateRequiredShape(opponentShape, expectedOutcome)
        gameResultPart2 = playGame(myShapePart2, opponentShape)
        gameScorePart2 = myShapePart2.value + gameResultPart2.value

        solutionPart1 += gameScorePart1
        solutionPart2 += gameScorePart2

    print(f"Solution part 1: {solutionPart1}")
    print(f"Solution part 2: {solutionPart2}")
