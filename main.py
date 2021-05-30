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
    results = []                        #create array for all results 

    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, machine, "ver: "+str(version), release, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "all: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed),storageTag, storageDevice]            #store all spec
    results += compList

    singleResult = runSingleCPU()       #run a single core cpu benchmark
    results.append("singleCPU: "+str(singleResult))        #store the result
    
    multiResult = spawnMultiProcess()          #run a multi core cpu benchmark
    results.append("multiCPU: "+str(multiResult))           #store the result
    
    memoryResult = runMemoryTest()      #run the memory usage test
    results.append("memory: "+str(memoryResult))        #store the result
    
    runWriteCSV(results)                #store all the reults in the csv

if __name__ == '__main__':
    main()  #call main to start program
