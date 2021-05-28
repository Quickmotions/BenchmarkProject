import multiprocessing
from multiprocessing import Queue
import math
import time
    
def multiProcess():
    starttime = time.time() # start timer
    count = 0
   
    while count < 50000: # run x amount of calculations (x can be adjusted to get diffrent scores)
        piValue = 2 ** count        #(2*increasing value) increasing value increases by 1 each loop and loops for x amount
        count += 1
    timeTaken = round(float(time.time() - starttime), 3)
    times.append(timeTaken)

def runMultiCPU(physCore):
    global times
    times = []
    queue = Queue()
    processes = []
    for _ in range(physCore): #the underscore signifies a throw away variable one which is discarded and not stored
        p = multiprocessing.Process(target=multiProcess, args=[queue]) #create 10 processes in a array named processes and tell it how many seconds to take.
        p.start()        #starts process for each core
        processes.append(p)       #adds this process to the list
    
    for process in processes:
        process.join()#joins all processes so that code doesnt run past until all are done

  
    
   
