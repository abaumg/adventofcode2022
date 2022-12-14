from enum import Enum
from math import floor
import os


class Monkey:
    def __init__(
        self,
        number=0,
        items=[],
        operation=None,
        testDivisibleBy=None,
        destinationMonkeys=(),
    ):
        self.number = number
        self.items = items
        self.operation = operation
        self.testDivisibleBy = testDivisibleBy
        self.destinationMonkeys = destinationMonkeys

    def __repr__(self):
        return f"Monkey(number={self.number}, items={self.items}, operation={self.operation}, testDivisibleBy={self.testDivisibleBy}, destinationMonkeys={self.destinationMonkeys})"


class OperationType(Enum):
    ADDITION = "+"
    MULTIPLICATION = "*"


class Operation:
    def __init__(self, operationType: OperationType, operands: tuple):
        self.operationType = operationType
        self.operands = operands

    def __repr__(self):
        return (
            f"Operation(operationType={self.operationType}, operands={self.operands})"
        )

    def execute(self):
        if self.operationType == OperationType.ADDITION:
            return self.operands[0] + self.operands[1]
        else:
            return self.operands[0] * self.operands[1]


class Item:
    def __init__(self, worryLevel):
        self.worryLevel = worryLevel

    def __repr__(self):
        return f"Item(worryLevel={self.worryLevel})"

    def inspect(self):
        self.worryLevel = floor(self.worryLevel / 3)


with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    rawMonkeys = inputFile.read().split("\n\n")

monkeys = []

for rawMonkey in rawMonkeys:
    for row in rawMonkey.split("\n"):
        if row.startswith("Monkey "):
            number = row.split(" ")[1][0]

        elif row.startswith("  Starting items"):
            items = [int(x) for x in row.split(":")[1].split(", ")]

        elif row.startswith("  Operation"):
            operand1, operator, operand2 = row.split(" ")[5:]
            operation = Operation(OperationType(operator), (operand1, operand2))

        elif row.startswith("  Test"):
            testDivisibleBy = row.split(" ")[-1]

        elif row.startswith("    If "):
            if "true:" in row:
                trueMonkey = int(row.split(" ")[-1])
            else:
                falseMonkey = int(row.split(" ")[-1])

    monkeys.append(
        Monkey(number, items, operation, testDivisibleBy, (trueMonkey, falseMonkey))
    )

print(monkeys)
