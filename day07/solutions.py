import os

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"

class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.totalSize = 0

    def __repr__(self):
        return f"Directory(name={self.name}, parent={self.parent}, children={self.children}, totalSize={self.totalSize})"

    def addChild(self, child):
        self.children.append(child)
        for child in self.children:
          child.parent = self

    def getChildByName(self, childname):
        if childname == "/":
            return self
        y = [x for x in filter(lambda x: x.name == childname and isinstance(x, Directory), self.children)]
        return y[0]

    def getSubdirectories(self):
        subdirectories = []
        for child in self.children:
            if isinstance(child, Directory):
                subdirectories.append(child)
                subdirectories += child.getSubdirectories()
        return subdirectories


def calcSize(elems):
    totalsize = 0
    for elem in elems:
        if isinstance(elem, File):
            totalsize += int(elem.size)
        else:
            totalsize += calcSize(elem.children)
    return totalsize
        


tree = Directory(name="/")

with open(f"{os.path.dirname(__file__)}/input.txt", "r") as inputFile:
    lines = [line.rstrip() for line in inputFile.readlines()]

# build tree
currentNode = tree
for line in lines:
    if line.startswith("$"):
        if line[2:4] == "ls":
            continue

        elif line[2:4] == "cd":
            targetDirectory = line[4:].strip()
            if targetDirectory == "..":
                currentNode = currentNode.parent
            else:
                currentNode = currentNode.getChildByName(targetDirectory)
        else:
            raise Exception("Unexpected content")
    else:
        dirOrSize, name = line.split(" ")
        if dirOrSize == "dir":
            currentNode.addChild(Directory(name=name))
        else:
            currentNode.addChild(File(name=name, size=dirOrSize))


solutionPart1 = 0
solutionPart2 = 0

subdirectoriesSums = list(map(lambda x: calcSize([x]), tree.getSubdirectories()))
filteredSums = [x for x in filter(lambda x: x <= 100000, subdirectoriesSums)]
solutionPart1 = sum(filteredSums)

USEDSIZE = calcSize([tree])
DISKSIZE = 70000000
REQUIREDFREESIZE =30000000
requireddeletion = REQUIREDFREESIZE - (DISKSIZE - USEDSIZE)
solutionPart2 = min([x for x in filter(lambda x: x >= requireddeletion, sorted(subdirectoriesSums))])

print(f"Solution part 1: {solutionPart1}")
print(f"Solution part 2: {solutionPart2}")