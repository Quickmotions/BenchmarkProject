def main():
    results = []
    from getComp import runGetComp
    from multiCPU import runMultiCPU
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    from memoryTest import runMemoryTest
    cpuBrand, OSBrand = runGetComp()
    results.append(cpuBrand)
    results.append(OSBrand)
    singleResult = runSingleCPU()
    results.append(singleResult)
    memoryResult = runMemoryTest()
    results.append(memoryResult)
    runMultiCPU()
    runWriteCSV(results)



main()
