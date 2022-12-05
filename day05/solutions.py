import os
import pandas as pd
from io import StringIO

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    crateContent = StringIO()
    instructionsContent = StringIO()
    for line in inputFile:
        if "[" in line:
            crateContent.write(line)
        elif "move" in line:
            instructionsContent.write(line)
        else:
            pass

    crateContent.seek(0)
    instructionsContent.seek(0)

crates = pd.read_fwf(crateContent, header=None)

stacks = {}
for n in range(1, len(crates.columns) + 1):
    stacks[str(n)] = crates[n - 1].dropna().to_list()

for instruction in instructionsContent.readlines():
    _, numberOfCrates, _, sourceIdx, _, destinationIdx = instruction.strip().split(" ")
    numberOfCrates = int(numberOfCrates)
    sourceDict = stacks[sourceIdx]
    destinationDict = stacks[destinationIdx]

    remainingSource = sourceDict[numberOfCrates:]
    cratesToMove = sourceDict[0:numberOfCrates]
    cratesToMove.reverse()
    destinationAfterMoving = cratesToMove + destinationDict

    stacks[sourceIdx] = remainingSource
    stacks[destinationIdx] = destinationAfterMoving

solutionPart1 = "".join([val[0][1:2] for _, val in stacks.items()])

print(f"Solution part 1: {solutionPart1}")
