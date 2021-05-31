def runMemoryTest():
    print("DEBUG: begun memtest")
    from memory_profiler import memory_usage                #import memory profiler package
    mem_usage = memory_usage(-1, interval=.5, timeout=10)   #run a test every .5 sec for 10 sec (mem_usage is array of results)
    AVGmem_usage = round(sum(mem_usage) / 20, 2)            #find the average of the 20 results and round to 2 decimal
    print("DEBUG MEMORY: " + str(AVGmem_usage))
    score = round(10000 / AVGmem_usage)                     #create a score by dividing 10000 by the avg memory usage.
    return score                                            #return the score to the main program.
