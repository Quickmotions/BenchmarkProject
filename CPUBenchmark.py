#---------------------------
#       05/04/21
#    CPU Benchmark
#   F Haak, C Gourlay
#---------------------------
import psutil
from cpuinfo import get_cpu_info
import platform
from uuid import getnode as get_mac
import time
import multiprocessing
import csv
import math
multicoreScores = 0
score = 1
num = 2
scores = []
sNext = 100
def multiProcess(): #starts process on single core
    scores = []
    score = 1
    cpu = psutil.cpu_percent(interval=0.0000001)
    for _ in range(1000):
        while cpu < 50:
            cpu = psutil.cpu_percent(interval=0.0)
            num = 2**score
            score += 1
        scores.append(score)
        cpu = 0
        score = 0
    value = 0
    value += math.floor(sum(scores) / len(scores))
    addScores(value)
    
def addScores(value):
    global multicoreScores
    multicoreScores = multicoreScores + value

if __name__ == '__main__':
    #singleprocessing
    print("Starting single-core benchmark on: ", get_cpu_info()['brand_raw'])
    cpu = psutil.cpu_percent(interval=0.0000001)
    starttime = time.time()
    for x in range(1000):
        while cpu < 50:
            cpu = psutil.cpu_percent(interval=0.0)
            num = 2**score
            score += 1
        scores.append(score)
        if x == sNext:
            print(sNext / 10, "% done")
            sNext += 100
        cpu = 0
        score = 0
    
    singleCPUScore = math.floor(sum(scores) / len(scores)) #math.floor rounds down
    print("done")
    timeTaken = round((time.time() - starttime), 4), ' Seconds'
    print('Time taken = ', timeTaken)
    print()
    
    #multiprocessing
    cores = int(multiprocessing.cpu_count() /2)
    print("Starting multi-core benchmark on: ", get_cpu_info()['brand_raw'], ' on ', cores, ' physical cores')
    start = time.perf_counter()

    processes = []
    

    for _ in range(cores): #the underscore signifies a throw away variable one which is discarded and not stored
        p = multiprocessing.Process(target=multiProcess, args=[]) #create 10 processes in a array named processes and tell it how many seconds to take.
        p.start()        #starts process for each core
        processes.append(p)       #adds this process to the list
    
    for process in processes:
        process.join()#joins all processes so that code doesnt run past until all are done

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    
    
    multiCPUScore = multicoreScores

    #results
    print(platform.processor())
    benchmarkID = get_mac()
    system = platform.system()
    gpuScore = 9.99
    storageScore = 9.99
    ramScore = 9.99
    overallScore = 9.99
    cpuDetails = get_cpu_info()['brand_raw']
    
    with open('data_container.csv', 'a', newline ='') as x:
        file_writer = csv.writer(x)
        file_writer.writerow([benchmarkID,system,singleCPUScore,multiCPUScore,gpuScore,storageScore,ramScore,overallScore,cpuDetails])

    print("----------------------------------")
    print("CPU single-core score: ", singleCPUScore)
    print("----------------------------------")
    print("CPU multi-core score: ", multiCPUScore)
    print("----------------------------------")

# print("type 1 to view technical cpu info")
# request = input("type 2 to see all scores: ")
# if request == "2":
#     print(scores)
# if request == "1":
#     print(get_cpu_info())







