def runWriteCSV(results):
    
    import csv          #import csv read/writer
    import cryptography #import encryption package

    with open('csv_files/data_container.csv', 'a', newline ='') as file: #open/create new file
        file_writer = csv.writer(file)  #select csv writer
        file_writer.writerow(results)   #write the results into the csv
