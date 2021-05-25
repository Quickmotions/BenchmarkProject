def runSingleCPU():
    import time
    import math
    starttime = time.time() # start timer
    count = 0
    while count < 50000: # run x amount of calculations
        piValue = 2 ** count
        count += 1
    timeTaken = round(float(time.time() - starttime), 3) #find time taken for x calculations to perform.
    if timeTaken > 1:
        score = 1000 / timeTaken
    else:
        score = 1000
    return round(score)
