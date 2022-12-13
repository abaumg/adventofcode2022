import os
import pandas as pd
from typing import List, Union

solutionPart1 = 0  # number of visible trees outside the grid
solutionPart2 = 0  # highest scenic score

gridWidth = 99

df = pd.read_fwf(
    f"{os.path.dirname(__file__)}/input.txt",
    widths=[1 for x in range(gridWidth)],
    header=None,
)


def calculateViewingDistance(
    treeHeight: int, treesAround: Union[None, List[int]]
) -> int:
    viewingDistance = 0
    if treesAround:
        for tree in treesAround:
            if tree >= treeHeight:
                viewingDistance += 1
                break
            else:
                viewingDistance += 1

    return viewingDistance


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

        scenicScore = 0

        distances = [len(x) for x in [treesTop, treesBottom, treesLeft, treesRight]]
        if min(distances) == 0:  # tree is on the edge
            solutionPart1 += 1
        else:
            maxHeightAround = [
                max(x) for x in [treesTop, treesBottom, treesLeft, treesRight]
            ]
            if currentTreeHeight > min(maxHeightAround):
                solutionPart1 += 1

        # part 2
        if columnIndex == 3 and currentTreeHeight == 5:
            print(currentColumn)
        viewingDistanceTop = calculateViewingDistance(
            currentTreeHeight, list(reversed(treesTop))
        )
        viewingDistanceBottom = calculateViewingDistance(currentTreeHeight, treesBottom)
        viewingDistanceLeft = calculateViewingDistance(
            currentTreeHeight, list(reversed(treesLeft))
        )
        viewingDistanceRight = calculateViewingDistance(currentTreeHeight, treesRight)

        scenicScore = (
            viewingDistanceTop
            * viewingDistanceBottom
            * viewingDistanceLeft
            * viewingDistanceRight
        )
        solutionPart2 = scenicScore if scenicScore > solutionPart2 else solutionPart2


print(f"Solution part 1: {solutionPart1}")
print(f"Solution part 2: {solutionPart2}")
