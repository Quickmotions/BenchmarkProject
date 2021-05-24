def main():
    results = []
    from GetComp import runGetComp
    from multiCPU import runMultiCPU
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    cpuBrand, OSBrand = runGetComp()
    results.append(cpuBrand)
    results.append(OSBrand)
    singleResult = runSingleCPU()
    results.append(singleResult)
    runMultiCPU()
    runWriteCSV(results)

main()
