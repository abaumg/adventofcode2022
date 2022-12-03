import os
from string import ascii_lowercase, ascii_uppercase

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    rucksacks = inputFile.read().splitlines()
    alphabet = list("*" + ascii_lowercase + ascii_uppercase)
    prioritiesSum = 0

    for rucksackContent in rucksacks:
        compartment1 = rucksackContent[: len(rucksackContent) // 2]
        compartment2 = rucksackContent[len(rucksackContent) // 2 :]

        commonItem = list(set(compartment1) & set(compartment2))

        prioritiesSum += alphabet.index(commonItem[0])

    print(f"The sum of priorities is {prioritiesSum}")
