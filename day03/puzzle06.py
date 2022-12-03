import os
from string import ascii_lowercase, ascii_uppercase

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    rucksacks = inputFile.read().splitlines()
    alphabet = list("*" + ascii_lowercase + ascii_uppercase)
    prioritiesSum = 0

    for rucksackGroup in range(0, len(rucksacks) // 3):
        rucksack1, rucksack2, rucksack3 = rucksacks[
            rucksackGroup * 3 : rucksackGroup * 3 + 3
        ]

        commonItem = list(set(rucksack1) & set(rucksack2) & set(rucksack3))

        prioritiesSum += alphabet.index(commonItem[0])

    print(f"The sum of priorities is {prioritiesSum}")
