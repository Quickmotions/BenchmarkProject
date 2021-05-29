
from multiprocessing import Process
import time

def print_func():
    print("done")

if __name__ == "__main__":  # confirms that the code is under main function
    start = time.perf_counter()
    procs = []
    # proc = Process(target=print_func)  # instantiating without any argument
    # procs.append(proc)
    # proc.start()

    # instantiating process with arguments
    for _ in range(10): 
        # print(name)
        proc = Process(target=print_func)
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)') 