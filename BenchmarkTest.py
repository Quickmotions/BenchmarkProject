import psutil
score = 1
num = 2
scores = []
next = 100
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
print("CPU final score average: ", finalScore)
request = input("type 1 to see all scores")
if request == "1":
    print(scores)
    








