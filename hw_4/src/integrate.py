from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import logging
import time

n_iter = 10000000

logging.basicConfig(
    filename="artifacts/integrate.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def integrate(f, a, b, n):
    acc = 0
    step = (b - a) / n
    for i in range(n):
        acc += f(a + i * step) * step
    
    logging.info(f"integrate a: {a:.2f}\t b: {b:.2f}\t res: {acc:.2f}")
    return acc

def calc_time(func, args):
    start = time.time()
    func(*args)
    return time.time() - start

def run_sync(f, a, b, n=n_iter):
    return integrate(f, a, b, n)

def run_with_threads(f, a, b, n_jobs):
    step = (b - a) / n_jobs
    ranges = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    results = []

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate, f, r[0], r[1], n_iter // n_jobs) for r in ranges]
        for future in futures:
            results.append(future.result())

    return sum(results)

def run_with_processes(f, a, b, n_jobs):
    step = (b - a) / n_jobs
    ranges = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    results = []

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate, f, r[0], r[1], n_iter // n_jobs) for r in ranges]
        for future in futures:
            results.append(future.result())

    return sum(results)