def runMemoryTest():
    from memory_profiler import memory_usage
    mem_usage = memory_usage(-1, interval=.5, timeout=10)
    AVGmem_usage = round(sum(mem_usage) / 20, 2)
    score = round(10000 / AVGmem_usage)
    return score