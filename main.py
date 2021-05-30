try:
    from UI import *
    from getComp import runGetComp
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    from memoryTest import runMemoryTest
    from multiCPU import spawnMultiProcess
    from tkinter import *
    import time
    
except:
    print("missing packages")
    exit()

def main():
    # hideButton()
    #create array for all results
    results = []                      
    changeTxt("Collecting system information...")
    #get all system info and store in a list, concatonate list into results
    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, machine, "ver: "+str(version), release, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "threads: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed),storageTag, storageDevice]            #store all spec
    results += compList
    
    #add values of each test
    changeTxt("Testing single-core capabilities of CPU")
    results.append("singleCPU: "+str(runSingleCPU()))      
    changeTxt("Testing multi-core capabilities of CPU")
    results.append("multiCPU: "+str(spawnMultiProcess()))
    changeTxt("Testing memory")  
    results.append("memory: "+str(runMemoryTest()))   
    changeTxt("done")     
    #store all the reults in the csv     
    runWriteCSV(results)
    time.sleep(1)
    exit()           
# makeShowButton()
if __name__ == '__main__':
    createUI()

