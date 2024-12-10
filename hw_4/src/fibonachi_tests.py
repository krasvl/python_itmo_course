import os
import pytest
from fibonachi import calc_time, fibonacci, run_sync, run_with_processes, run_with_threads

def test_fibonacci_base():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5

@pytest.mark.parametrize("n_tasks", [5, 10, 20])
def test_fibonacci_performance_30_5(n_tasks):
    os.makedirs("artifacts", exist_ok=True)
    n = 30

    sync_time = calc_time(run_sync, [n, n_tasks])
    with open(f"artifacts/fibonachi.txt", "a") as f:
        f.write(f"Sync\t exec time for n: {n}\t n_tasks: {n_tasks}\t res: {sync_time:.2f} sec\n")

    threads_time = calc_time(run_with_threads, [n, n_tasks])
    with open(f"artifacts/fibonachi.txt", "a") as f:
        f.write(f"Thread\t exec time for n: {n}\t n_tasks: {n_tasks}\t res: {threads_time:.2f} sec\n")

    processes_time = calc_time(run_with_processes, [n, n_tasks])
    with open(f"artifacts/fibonachi.txt", "a") as f:
        f.write(f"Process\t exec time for n: {n}\t n_tasks: {n_tasks}\t res: {processes_time:.2f} sec\n\n")

    assert os.path.exists(f"artifacts/fibonachi.txt")