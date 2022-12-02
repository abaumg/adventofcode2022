with open("input.txt", "r") as inputFile:
    elves = inputFile.read().split("\n\n")

    highestCaloriesAmount = 0

    for elfChunk in elves:
        caloriesList = [int(calories) for calories in elfChunk.splitlines()]
        caloriesAmount = sum(caloriesList)

        highestCaloriesAmount = (
            caloriesAmount
            if caloriesAmount > highestCaloriesAmount
            else highestCaloriesAmount
        )

    print(f"Highest calories amount: {highestCaloriesAmount}")
