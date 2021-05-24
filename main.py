def main():
    results = []
    from getComp import runGetComp
    from multiCPU import runMultiCPU
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    cpuBrand, OSBrand = runGetComp()
    singleResult = runSingleCPU()
    results.append(singleResult)
    runMultiCPU()
    runWriteCSV(results)

main()
