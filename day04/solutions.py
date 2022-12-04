import os

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:

    solutionpart1 = 0
    for pairs in inputFile.read().splitlines():
        pair1, pair2 = list(sorted(pairs.split(",")))
        pair1start, pair1end = map(int, pair1.split("-"))
        pair2start, pair2end = map(int, pair2.split("-"))
        range1 = range(pair1start, pair1end)
        range2 = range(pair2start, pair2end)

        if (range1.start <= range2.start and range1.stop >= range2.stop) or (
            range2.start <= range1.start and range2.stop >= range1.stop
        ):
            solutionpart1 += 1

    print(f"Solution part 1: {solutionpart1}")
