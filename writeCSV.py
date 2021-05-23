# runs the import to bring in the csv settings required
import csv

def runWriteCSV():
# printing to file 
    with open('.../csv_files/data_container.csv', 'a', newline ='') as x:
        file_writer = csv.writer(x)
        file_writer.writerow([results[0],results[1],results[2],results[3],results[4],results[5],results[6],results[7],results[8]])
