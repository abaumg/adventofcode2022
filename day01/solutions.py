import os

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    elves = inputFile.read().split("\n\n")

    solutionPart1 = 0
    totalCaloriesAmounts = []

    for elfChunk in elves:
        caloriesList = [int(calories) for calories in elfChunk.splitlines()]
        caloriesAmount = sum(caloriesList)
        totalCaloriesAmounts.append(sum(caloriesList))

        solutionPart1 = (
            caloriesAmount if caloriesAmount > solutionPart1 else solutionPart1
        )

    solutionPart2 = sum(sorted(totalCaloriesAmounts, reverse=True)[0:3])

    print(f"Solution part 1: {solutionPart1}")
    print(f"Solution part 2: {solutionPart2}")
