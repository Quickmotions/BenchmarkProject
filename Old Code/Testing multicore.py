import multiprocessing #allows use of multiple cores
import time

def do_something(): #spend 1 sec
    print('sleeping 1 second...')
    time.sleep(0.5)
    print('done sleeping...')
    
if __name__ == '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something) #creates first procces
    p2 = multiprocessing.Process(target=do_something) #creates second process at same time
   
    
    p1.start()
    p2.start()#starts both processes at same time does not wait to continue onto rest of code

    p1.join() 
    p2.join() #stops code until process is finnished

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)') 


#here we run both tasks at once so that it only takes 1 sec instead of 2 since do_somthing is running in parrallel