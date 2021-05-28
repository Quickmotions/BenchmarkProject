def createKey():
    from cryptography.fernet import Fernet  #import encryption package

    key = Fernet.generate_key() #create encryption key
    
    with open('filekey.key', 'wb') as filekey:  #open a key file
        filekey.write(key)                      #write the key into the file (ex. key: J64ZHFpCWFlS9zT7y5zxuQN1Gb09y7cucne_EhuWyDM=)    

        
        
        
        
def encryptResults(results):       #encrypt the file using fernet
    
    from cryptography.fernet import Fernet  #import encryption package
    
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open('csv_files/data_container.csv', 'rb') as file:
        results = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(results)

    # opening the file in write mode and 
    # writing the encrypted data
    with open('csv_files/data_container_encrypted.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
      
        
def runWriteCSV(results):
    import csv   #import csv read/writer
    createKey()  #create a key and store it
    
    with open('csv_files/data_container.csv', 'a', newline ='') as file: #open/create new file
        file_writer = csv.writer(file)  #select csv writer
        file_writer.writerow(results)   #write the results into the csv
       
    encryptResults(results)                #encrypt the results into a diffrent csv
    from sendCSV import runSendCSV  #import the script for sending csv to server
    runSendCSV()    #send csv to server
    print("Done")   #end write
