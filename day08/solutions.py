import os
import pandas as pd

solutionPart1 = 0

gridWidth = 99

df = pd.read_fwf(
    f"{os.path.dirname(__file__)}/input.txt",
    widths=[1 for x in range(gridWidth)],
    header=None,
)

gridHeight = len(df)
for columnIndex in range(0, gridHeight):
    currentColumn = df.iloc[columnIndex : columnIndex + 1]

    for rowIndex in range(0, gridWidth):
        currentRow = df[rowIndex]
        currentTreeHeight = currentColumn[rowIndex].iloc[0]

        treesTop = list(currentRow[:columnIndex])
        treesBottom = list(currentRow[columnIndex + 1 :])
        treesLeft = list(currentColumn.iloc[0, :rowIndex])
        treesRight = list(currentColumn.iloc[0, rowIndex + 1 :])

        distances = [len(x) for x in [treesTop, treesBottom, treesLeft, treesRight]]
        if min(distances) == 0:  # tree is on the edge
            solutionPart1 += 1
            continue

        maxHeightAround = [
            max(x) for x in [treesTop, treesBottom, treesLeft, treesRight]
        ]
        if currentTreeHeight > min(maxHeightAround):
            solutionPart1 += 1
            continue

print(f"Solution part 1: {solutionPart1}")
