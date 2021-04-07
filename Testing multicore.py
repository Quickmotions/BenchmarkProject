if __name__ == '__main__': #used to allow or prevent parts of code from being run when the modules are imported.
    import time

    start = time.perf_counter()

    def do_something(): #spend 1 sec
        print('sleeping 1 second...')
        time.sleep(1)
        print('done sleeping...')

    do_something()#runs once takes 1 sec, if done twice it will take 2 sec.
    do_something()#runs after the one before

    finnish = time.perf_counter()

    print(f'Finnished in {round(finnish-start, 2)} second(s)') 
    #finnishes in 1 sec since it only does do-something once, if it was run twice it would take 2 secs.

#here we run both tasks at once so that it only takes 1 sec instead of 2 since do_somthing is running in parrallel