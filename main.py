def main():
    results = ["linux", "intel i8", 123, 234]
    
    from multiCPU import runMultiCPU
    from singleCPU import runSingleCPU
    from writeCSV import runWriteCSV
    runSingleCPU()
    runMultiCPU()
    runWriteCSV(results)

main()
