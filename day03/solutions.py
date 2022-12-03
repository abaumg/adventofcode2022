import os
from string import ascii_lowercase, ascii_uppercase

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    rucksacks = inputFile.read().splitlines()
    alphabet = list("*" + ascii_lowercase + ascii_uppercase)
    solutionPart1 = 0
    solutionPart2 = 0

    for rucksackContent in rucksacks:
        compartment1 = rucksackContent[: len(rucksackContent) // 2]
        compartment2 = rucksackContent[len(rucksackContent) // 2 :]

        commonItem = list(set(compartment1) & set(compartment2))

        solutionPart1 += alphabet.index(commonItem[0])

    for rucksackGroup in range(0, len(rucksacks) // 3):
        rucksack1, rucksack2, rucksack3 = rucksacks[
            rucksackGroup * 3 : rucksackGroup * 3 + 3
        ]

        commonItem = list(set(rucksack1) & set(rucksack2) & set(rucksack3))

        solutionPart2 += alphabet.index(commonItem[0])

    print(f"Solution part 1: {solutionPart1}")
    print(f"Solution part 2: {solutionPart2}")
