def getSignalMarker(filename):
    f = open(filename, 'r')
    buffer = f.readline()

    currentChar = 0
    readingFrame = 4

    while(currentChar < len(buffer) + readingFrame):
        signal = []

        for i in range(readingFrame):
            if(buffer[currentChar + i] not in signal):
                signal.append(buffer[currentChar + i])

        if(len(signal) != readingFrame):
            currentChar += 1
        else:
            break

    print(f'The packet marker was detected after {currentChar + readingFrame} ' +
          'characters were processed')


getSignalMarker('input.txt')
