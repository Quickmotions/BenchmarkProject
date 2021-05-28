import multiprocessing
from multiprocessing import Queue
import math
import time
    
def multiProcess():
    count = 0
    while count < 50000: # run x amount of calculations (x can be adjusted to get diffrent scores)
        piValue = 2 ** count        #(2*increasing value) increasing value increases by 1 each loop and loops for x amount
        count += 1
    

def runMultiCPU():
    if __name__ == '__main__':
        
        processes = []
        startT = time.perf_counter()
        for _ in range(100): #the underscore signifies a throw away variable one which is discarded and not stored
            p = multiprocessing.Process(target=multiProcess) #create 10 processes in a array named processes and tell it how many seconds to take.
            p.start()        #starts process for each core
            processes.append(p)       #adds this process to the list
        
        for process in processes:
            process.join()#joins all processes so that code doesnt run past until all are done
        timeTaken = round(time.perf_counter() - startT, 2)
        print(timeTaken)
        score = round(10000 /timeTaken)
        print(score)
        return(score)

   
