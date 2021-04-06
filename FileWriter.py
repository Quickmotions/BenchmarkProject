import csv

benchmarkID = ""
cpu_score = 0.0
gpu_score = 0.0
storage_score = 0.0
ram_score = 0.0
oversll_score = 0.0

with open('data_container.csv', 'w', newline ='') as x:
    fieldnames = ['CPU Score', 'GPU Score', 'Storage Score', 'RAM Score', 'Overall Score']
    file_writer = csv.writer(x, fieldnames=fieldnames)
    file_writer.writeheader()
