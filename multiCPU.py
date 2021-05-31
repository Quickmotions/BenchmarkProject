def multiProcess():
    count = 0
    while count < 10000: # run x amount of calculations (x can be adjusted to get diffrent scores)
         piValue = 2 ** count        #(2*increasing value) increasing value increases by 1 each loop and loops for x amount
         count += 1

def spawnMultiProcess():
    if __name__ == 'multiCPU':  # confirms that the code is under main function
        from multiprocessing import Process
        import time
        print("DEBUG: begun multiCPU")
        start = time.perf_counter()
        procs = []
        # instantiating process with arguments
        for _ in range(100): 
            proc = Process(target=multiProcess)
            procs.append(proc)
            proc.start()

        # complete the processes
        for proc in procs:
            proc.join()

        timeTaken = round(time.perf_counter() - start, 2)
        print("DEBUG multitime: " + str(timeTaken))
        return round(10000 /timeTaken/10)


   
