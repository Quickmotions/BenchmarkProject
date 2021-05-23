# runs the import to bring in the csv settings required
import csv

# Declaring String Variables
benchmarkID = "Placeholder"
system = "Placeholder"
cpuDetails = "Placeholder"
# Declaring Float Variables
cpuScore = 0.00
gpuScore = 0.00
storageScore = 0.00
ramScore = 0.00
overallScore = 0.00
multiCPUScore = 0.00
singleCPUScore = 0.00

def WriteCSV():
# printing to file 
    with open('.../csv_files/data_container.csv', 'a', newline ='') as x:
        file_writer = csv.writer(x)
        file_writer.writerow([benchmarkID,system,singleCPUScore,multiCPUScore,gpuScore,storageScore,ramScore,overallScore,cpuDetails])
