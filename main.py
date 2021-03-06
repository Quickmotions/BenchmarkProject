from subprocess import run


#attempt to import all packages
from UI import *
from getComp import runGetComp
from singleCPU import runSingleCPU
from writeCSV import runWriteCSV
from memoryTest import runMemoryTest
from multiCPU import spawnMultiProcess
from diskTest import runDiskTest
import time
    


def mainProgram():
    # start timer
    start = time.perf_counter() 
    #create array for all results
    results = []                      
    changeTxt("Collecting system information...")#update UI
    #get all system info and store in a list, concatonate list into results
    systemTag, system, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed= runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "threads: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed)]            #store all spec
    results += compList
    
    #add values of each test
    changeTxt("Testing single-core capabilities of CPU") #update ui
    results.append("singleCPU: "+str(runSingleCPU()))      
    changeTxt("Testing multi-core capabilities of CPU") #update ui
    results.append("multiCPU: "+str(spawnMultiProcess()))
    changeTxt("Testing memory")                         #update ui
    results.append("memory: "+str(runMemoryTest()))
    changeTxt("Testing Disk Usage")                         #update ui
    disks, sizes = runDiskTest()
    diskList = ""
    for disk in range(len(disks)):
        diskList += str(disks[disk]) + " : " + str(sizes[disk] + " | ")
    results.append(diskList)
    time.sleep(1)  
    changeTxt("done in: " + str(round(time.perf_counter() - start, 2)) + " secs")     #update ui
    #store all the reults in the csv     
    runWriteCSV(results)
    time.sleep(1)   #wait 1 sec for user to read "done" text
    exit()             #close program

if __name__ == '__main__': #if this is main program create the ui
    createUI()
    