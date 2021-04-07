#---------------------------
#       05/04/21
#   Singlecore CPU
#       Benchmark
#   F Haak, C Gourlay
#---------------------------
import psutil
from cpuinfo import get_cpu_info
import platform
from uuid import getnode as get_mac
import time
import multiprocessing
import csv
score = 1
num = 2
scores = []
sNext = 100

def multiProcess(seconds): #spend 1 sec
    time.sleep(seconds)

if __name__ == '__main__':
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
    singleCPUScore = sum(scores) / len(scores)
    print("done")
    timeTaken = round((time.time() - starttime), 4), ' Seconds'
    print('Time taken = ', timeTaken)
    print()
    print("Starting multi-core benchmark on: ", get_cpu_info()['brand_raw'])
    start = time.perf_counter()

    processes = []
    mNext = 10

    for core in range(100):                                            #the underscore signifies a throw away variable one which is discarded and not stored
        p = multiprocessing.Process(target=multiProcess, args=[1])  #create 10 processes in a array named processes and tell it how many seconds to take.
        p.start()                                                   #starts all 10 processes
        processes.append(p)                                         #adds this process to the list
        if core == mNext:
            print(mNext, "% done")
            mNext += 10


    for process in processes:
        process.join()                                              #joins all processes so that code doesnt run past until all are done
    
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    multiTimeTaken = round(finish-start, 2)
    multiCPUScore = 100000 / multiTimeTaken

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
        file_writer.writerow([benchmarkID,system,timeTaken,singleCPUScore,multiCPUScore,gpuScore,storageScore,ramScore,overallScore,cpuDetails])

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







