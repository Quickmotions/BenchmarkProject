from GetComp import runGetComp
from multiCPU import runMultiCPU
from singleCPU import runSingleCPU
from writeCSV import runWriteCSV
from memoryTest import runMemoryTest

def main():
    
    results = []                        #create array for all results
    #importScripts()                     #call import scripts
    
    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore, maxFreq,minFreq ,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
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
    results.append(maxFreq)
    results.append(minFreq)
    results.append(memoryTag)
    results.append(memTotal)
    results.append(memUsed)
    results.append(storageTag)
    results.append(storageDevice)
 

    singleResult = runSingleCPU()       #run a single core cpu benchmark
    results.append(singleResult)        #store the result
    
    memoryResult = runMemoryTest()      #run the memory usage test
    results.append(memoryResult)        #store the result
    
    multiResult = runMultiCPU()          #run a multi core cpu benchmark
    results.append(multiResult)           #store the result
    
    runWriteCSV(results)                #store all the reults in the csv



main()  #call main to start program
