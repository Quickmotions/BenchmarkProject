if __name__ == '__main__':
    try:
        from getComp import runGetComp
        from singleCPU import runSingleCPU
        from writeCSV import runWriteCSV
        from memoryTest import runMemoryTest
        from multiCPU import spawnMultiProcess
        from multiprocessing import Process
        import time
    except:
        print("missing packages")
        exit()

def main():
    #create array for all results
    results = []                        

    #get all system info and store in a list, concatonate list into results
    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, machine, "ver: "+str(version), release, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "all: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed),storageTag, storageDevice]            #store all spec
    results += compList

    #add values of each test
    results.append("singleCPU: "+str(runSingleCPU()))      
    results.append("multiCPU: "+str(spawnMultiProcess()))  
    results.append("memory: "+str(runMemoryTest()))   
         
    #store all the reults in the csv     
    runWriteCSV(results)               


if __name__ == '__main__':
    main()  #call main to start program (if it is main and not a multiproccess)
