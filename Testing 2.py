if __name__ == '__main__': #used to allow or prevent parts of code from being run when the modules are imported.
    print("yes")
    import time

    start = time.perf_counter()

    def do_something():
        print('sleeping 1 second...')
        time.sleep(1)
        print('done sleeping...')

    do_something()
    
    finnish = time.perf_counter()

    print(f'Finnished in {round(finnish-start, 2)} second(s)')