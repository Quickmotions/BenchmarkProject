import psutil
from cpuinfo import get_cpu_info
import multiprocessing
import platform
score = 1
num = 2
scores = []
next = 100
print("Starting single-core benchmark on: ", get_cpu_info()['brand_raw'])
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
finalScore = sum(scores) / len(scores)
print("done")
print()
print(platform.processor())
("----------------------------------")
print("CPU final score average: ", finalScore)
print("----------------------------------")
print("type 1 to view technical cpu info")
request = input("type 2 to see all scores: ")
if request == "2":
    print(scores)
if request == "1":
    print(get_cpu_info())








