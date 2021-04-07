#---------------------------
#       07/04/21
#   Multicore CPU
#       Benchmark
#   F Haak, C Gourlay
#---------------------------
import psutil
from cpuinfo import get_cpu_info
import multiprocessing
import platform
import csv
score = 1
num = 2
scores = []
next = 100

def SingleBench():
    cpu = psutil.cpu_percent(interval=0.0000001)
    for x in range(1000):
        while cpu < 50:
            cpu = psutil.cpu_percent(interval=0.0)
            num = 2**score
            score += 1
        scores.append(score)
        if x == next:
            print(next / 10, "% done")
            next += 100 
        cpu = 0
        score = 0





print("Starting multi-core benchmark on: ", get_cpu_info()['brand_raw'])

cpuScore = sum(scores) / len(scores)
print("done")
print()
print(platform.processor())
benchmarkID = "Placeholder"
gpuScore = 9.99
storageScore = 9.99
ramScore = 9.99
overallScore = 9.99
cpuDetails = get_cpu_info()['brand_raw']

with open('data_container.csv', 'a', newline ='') as x:
    file_writer = csv.writer(x)
    file_writer.writerow([benchmarkID,cpuScore,gpuScore,storageScore,ramScore,overallScore,cpuDetails])

("----------------------------------")
print("CPU final score average: ", cpuScore)
print("----------------------------------")
# print("type 1 to view technical cpu info")
# request = input("type 2 to see all scores: ")
# if request == "2":
#     print(scores)
# if request == "1":
#     print(get_cpu_info())







