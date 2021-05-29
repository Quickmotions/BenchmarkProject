if __name__ == '__main__':
    try:
        from getComp import runGetComp
        from singleCPU import runSingleCPU
        from writeCSV import runWriteCSV
        from memoryTest import runMemoryTest
        from multiprocessing import Process
        import time
    except:
        print("missing packages")
        exit()

    
def multiProcess():
    count = 0
    while count < 5000: # run x amount of calculations (x can be adjusted to get diffrent scores)
         piValue = 2 ** count        #(2*increasing value) increasing value increases by 1 each loop and loops for x amount
         count += 1

def spawnMultiProcess():
    if __name__ == '__main__':  # confirms that the code is under main function
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
        print(timeTaken)
        return round(10000 /timeTaken/10)

def main():
    results = []                        #create array for all results 

    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo

    results.append(systemTag)            #store all spec
    results.append(system)
    results.append(machine)
    results.append(version)
    results.append(release)
    results.append(node)
    results.append(cpuTag)
    results.append(cpuBrand)
    results.append(physCore)
    results.append(allCore)
    results.append(memoryTag)
    results.append(memTotal)
    results.append(memUsed)
    results.append(storageTag)
    results.append(storageDevice)


    singleResult = runSingleCPU()       #run a single core cpu benchmark
    results.append(singleResult)        #store the result
    
    multiResult = spawnMultiProcess()          #run a multi core cpu benchmark
    results.append(multiResult)           #store the result
    
    memoryResult = runMemoryTest()      #run the memory usage test
    results.append(memoryResult)        #store the result
    
    runWriteCSV(results)                #store all the reults in the csv


if __name__ == '__main__':
    main()  #call main to start program
