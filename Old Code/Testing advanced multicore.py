from multiprocessing import Process #allows use of multiple cores
import time

def do_something(): #spend 1 sec
    print("done")
    
    
if __name__ == '__main__':
    start = time.perf_counter()

    processes = []

    for _ in range(10): #the underscore signifies a throw away variable one which is discarded and not stored
        p = Process(target=do_something) #create 10 processes in a array named processes and tell it how many seconds to take.
        processes.append(p)  
        p.start()         
    
    for process in processes:
        process.join()#joins all processes so that code doesnt run past until all are done


    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)') 


#here we run multiple process similaneouly using a loop finnishes in 2.4 sec instead of 10 sec