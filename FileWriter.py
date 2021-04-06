import csv

benchmarkID = "Placeholder"
cpu_score = 9.99
gpu_score = 9.99
storage_score = 9.99
ram_score = 9.99
overall_score = 9.99

with open('data_container.csv', 'a', newline ='') as x:
    file_writer = csv.writer(x)
    file_writer.writerow([benchmarkID,cpu_score,gpu_score,storage_score,ram_score,overall_score])
