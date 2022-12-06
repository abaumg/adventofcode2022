with open("input.txt", "r") as inputFile:
    byteStream = inputFile.read()
    packetMarkerLength = 4
    messageMarkerLength = 14
    solutionPart1 = 0
    solutionPart2 = 0
    for i in range(0, len(byteStream)):
        if solutionPart1 == 0:
            fourMostRecentlyReceivedCharacters = byteStream[i : i + packetMarkerLength]
            if len(set(fourMostRecentlyReceivedCharacters)) == packetMarkerLength:
                solutionPart1 = packetMarkerLength + i

        if solutionPart2 == 0:
            fourteenMostRecentlyReceivedCharacters = byteStream[i : i + messageMarkerLength]
            if len(set(fourteenMostRecentlyReceivedCharacters)) == messageMarkerLength:
                solutionPart2 = messageMarkerLength + i


    print(f"Solution part 1: {solutionPart1}")
    print(f"Solution part 2: {solutionPart2}")
