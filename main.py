try: #attempt to import all packages
    from UI import *
    from getComp import runGetComp
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    from memoryTest import runMemoryTest
    from multiCPU import spawnMultiProcess
    import time
    
except:
    #error message and close program
    print("missing packages")
    exit()

def main():
    # start timer
    start = time.perf_counter() 
    #create array for all results
    results = []                      
    changeTxt("Collecting system information...")#update UI
    #get all system info and store in a list, concatonate list into results
    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, machine, "ver: "+str(version), release, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "threads: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed),storageTag, storageDevice]            #store all spec
    results += compList
    
    #add values of each test
    changeTxt("Testing single-core capabilities of CPU") #update ui
    results.append("singleCPU: "+str(runSingleCPU()))      
    changeTxt("Testing multi-core capabilities of CPU") #update ui
    results.append("multiCPU: "+str(spawnMultiProcess()))
    changeTxt("Testing memory")                         #update ui
    results.append("memory: "+str(runMemoryTest()))   
    changeTxt("done in: " + str(round(time.perf_counter() - start, 2)) + " secs")     #update ui
    #store all the reults in the csv     
    runWriteCSV(results)
    time.sleep(1)   #wait 1 sec for user to read "done" text
    exit()             #close program

if __name__ == '__main__': #if this is main program create the ui
    createUI()
    