import time
import multiprocessing
import psutil
from cpuinfo import get_cpu_info
import platform
from uuid import getnode as get_mac
import csv
score = 1
num = 2
scores = []
next = 100




































# def StartBench(core):
#     for x in range(1000):
#         while cpu < 50:
#             cpu = psutil.cpu_percent(interval=0.0)
#             num = 2**score
#             score += 1
#         scores.append(score)
#         if x == next:
#             print(next / 10, "% done")
#             next += 100
            
#         cpu = 0
#         score = 0
    
      
# def multiprocessing_func(core):
#     time.sleep(2)
#     StartBench(core)
    
# if __name__ == '__main__':
#     print("Starting single-core benchmark on: ", get_cpu_info()['brand_raw'])
#     cpu = psutil.cpu_percent(interval=0.0000001)
#     starttime = time.time()
    
#     processes = []
#     for i in range(1,10):
#         p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
#         processes.append(p)
#         p.start()
        
#     for process in processes:
#         process.join()
        
#     print()    
#     print('Time taken = {} seconds'.format(time.time() - starttime))