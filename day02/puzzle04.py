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
    totalGameScore = 0
    for game in games:
        opponentShapeCode, expectedOutcomeCode = game.split(" ")
        expectedOutcome = mapCodeToOutcome(expectedOutcomeCode)
        opponentShape = mapCodeToShape(opponentShapeCode)
        myShape = calculateRequiredShape(opponentShape, expectedOutcome)
        gameResult = playGame(myShape, opponentShape)
        gameScore = myShape.value + gameResult.value

        totalGameScore += gameScore

    print(f"My total score would be {totalGameScore}")
