with open("input.txt", "r") as inputFile:
    byteStream = inputFile.read()
    chunkSize = 4
    for i in range(0, len(byteStream)):
        fourMostRecentlyReceivedCharacters = byteStream[i : i + chunkSize]
        if len(set(fourMostRecentlyReceivedCharacters)) > 3:
            print(f"Solution part 1: {i+chunkSize}")
            break
