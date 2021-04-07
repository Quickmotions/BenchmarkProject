import multiprocessing #allows use of multiple cores
import time

def do_something(): #spend 1 sec
    print('sleeping 1 second...')
    time.sleep(1)
    print('done sleeping...')
    
if __name__ == '__main__':
    start = time.perf_counter()

    for _ in range(10): #the underscore signifies a throw away variable one which is discarded and not stored
        p = multiprocessing.Process(target=do_something)
        p.start()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)') 


#here we run multiple process similaneouly using a loop