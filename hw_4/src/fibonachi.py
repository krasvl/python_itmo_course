import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calc_time(func, args):
    start = time.time()
    func(*args)
    return time.time() - start

def run_sync(n, n_tasks):
    for _ in range(n_tasks):
        fibonacci(n)

def run_with_threads(n, n_tasks):
    threads = []
    for _ in range(n_tasks):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def run_with_processes(n, n_tasks):
    processes = []
    for _ in range(n_tasks):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()