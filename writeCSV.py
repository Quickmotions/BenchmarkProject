# runs the import to bring in the csv settings required
import csv

def runWriteCSV(results):
    if __name__ == '__main__':
        with open('/csv_files/data_container.csv', 'a', newline ='') as file:
            file_writer = csv.writer(file) 
            file_writer.writerow(results)
