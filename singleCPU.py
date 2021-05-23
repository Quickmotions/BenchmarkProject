def runSingleCPU():
    import psutil
    import time
    import math
    starttime = time.time() # start timer
    count = 0
    while count < 100000:
        piValue = 2 ** count
        count += 1
    timeTaken = str(round((time.time() - starttime), 2)) + ' Seconds'
    print(timeTaken)