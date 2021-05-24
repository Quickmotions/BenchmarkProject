def runSingleCPU():
    import psutil
    import time
    import math
    starttime = time.time() # start timer
    count = 0
    while count < 100000: # run x amount of calculations
        piValue = 2 ** count
        count += 1
    timeTaken = round((time.time() - starttime, 3) #find time taken for x calculations to perform.
    print(str(timeTaken) + " seconds") #print seconds taken#
    return timeTaken
