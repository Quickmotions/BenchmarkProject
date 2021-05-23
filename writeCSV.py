import csv

# Declaring String Variables
benchmarkID = "Placeholder"
system = "Jo Momma"
cpuDetails = "Intel Core i25"
# Declaring Float Variables
cpuScore = 9.99
gpuScore = 9.99
storageScore = 9.99
ramScore = 9.99
overallScore = 9.99
multiCPUScore = 9.99
singleCPUScore = 9.99

 # printing to file
 with open('data_container.csv', 'a', newline ='') as x:
        file_writer = csv.writer(x)
        file_writer.writerow([benchmarkID,system,singleCPUScore,multiCPUScore,gpuScore,storageScore,ramScore,overallScore,cpuDetails])

# File commence printer
#with open('data_container.csv', 'a', newline ='') as x:
        #file_writer = csv.writer(x)
        #file_writer.writerow(["benchmarkID","System","Single CPU Score","Multi CPU Score","GPU Score","Storage Score","Ram Score","Overall Score","CPU Details"])