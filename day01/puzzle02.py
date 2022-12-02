import os

print(os.path.dirname(__file__))
with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    elves = inputFile.read().split("\n\n")

    totalCaloriesAmounts = []

    for elfChunk in elves:
        caloriesList = [int(calories) for calories in elfChunk.splitlines()]
        totalCaloriesAmounts.append(sum(caloriesList))

    topThreeCaloriesAmounts = sum(sorted(totalCaloriesAmounts, reverse=True)[0:3])
    print(
        f"Top three elves carry a total of {topThreeCaloriesAmounts} calories together"
    )
