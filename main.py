def importScripts():             #imports all scripts required
    from getComp import runGetComp
    from multiCPU import runMultiCPU
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    from memoryTest import runMemoryTest

def main():
    
    results = []                        #create array for all results
    importScripts()                     #call import scripts
    
    cpuBrand, OSBrand = runGetComp()    #collect all system and component imfo
    results.append(cpuBrand)            #store cpu brand raw
    results.append(OSBrand)             #store the operating system
    
    singleResult = runSingleCPU()       #run a single core cpu benchmark
    results.append(singleResult)        #store the result
    
    memoryResult = runMemoryTest()      #run the memory usage test
    results.append(memoryResult)        #store the result
    
    runMultiCPU()                       #run a multi core cpu benchmark
    results.append(0)#placeholder       #store the result
    
    runWriteCSV(results)                #store all the reults in the csv


importScripts() #imports the required scripts to start the program
main()  #call main to start program
