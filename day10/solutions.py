import os
import queue

solutionPart1 = 0

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    instructions = inputFile.readlines()

stack = queue.Queue()
cycle = 1
registerX = 1
sprite = range(0, 2)
crtRow = ""


# build stack
for instruction in instructions:
    instruction = instruction.strip()

    if instruction.startswith("noop"):
        stack.put(None)

    elif instruction.startswith("addx"):
        _, amount = instruction.split(" ")
        stack.put(None)
        stack.put(int(amount))

# process stack
while stack.qsize() > 0:
    # part 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signalStrength = cycle * registerX
        solutionPart1 += signalStrength

    # part 2
    pixelCurrentlyDrawn = (cycle % 40) - 1
    if pixelCurrentlyDrawn in sprite:
        crtRow += "#"
    else:
        crtRow += "."

    if len(crtRow) == 40:
        print(crtRow)
        crtRow = ""

    # process instruction
    instruction = stack.get()
    if instruction:
        registerX += instruction
        sprite = range(registerX - 1, registerX + 2)

    cycle += 1

print(f"Solution part 1: {solutionPart1}")
