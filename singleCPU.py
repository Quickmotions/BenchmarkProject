def runSingleCPU():
    print("DEBUG: begun singleCPU")
    import time
    import math
    starttime = time.time() # start timer
    count = 0
   
    while count < 50000: # run x amount of calculations (x can be adjusted to get diffrent scores)
        piValue = 2 ** count        #(2*increasing value) increasing value increases by 1 each loop and loops for x amount
        count += 1
    timeTaken = round(float(time.time() - starttime), 3) #find time taken for x calculations to perform.
    print("DEBUG singletime: " + str(timeTaken))
    #if time is < 1 then make the score max(10000) this is because if the time is less than 1 then the max score will be multiplied instead of reduced
    if timeTaken > 1:               
        score = 10000 / timeTaken   #to get score divide 10000 by the time it took to run x calculations
    else:
        score = 10000
    
    return round(score/10) #return the score and round to nearest whole
