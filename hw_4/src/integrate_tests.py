import math
import os
import pytest
from integrate import calc_time, integrate, run_sync, run_with_processes, run_with_threads

def test_integrate_base():
    assert abs(integrate(math.cos, 0, math.pi / 2, 10000) - 1) < 0.001

@pytest.mark.parametrize("n_tasks", [1, 2, 4, 8, 16])
def test_integrate_performance(n_tasks):
    os.makedirs("artifacts", exist_ok=True)

    sync_time = calc_time(run_sync, [math.cos, 0, math.pi / 2])
    with open(f"artifacts/integrate.txt", "a") as f:
        f.write(f"Sync\t exec time for n_tasks: {n_tasks}\t res: {sync_time:.2f} sec\n")

    threads_time = calc_time(run_with_threads, [math.cos, 0, math.pi / 2, n_tasks])
    with open(f"artifacts/integrate.txt", "a") as f:
        f.write(f"Thread\t exec time for n_tasks: {n_tasks}\t res: {threads_time:.2f} sec\n")

    processes_time = calc_time(run_with_processes, [math.cos, 0, math.pi / 2, n_tasks])
    with open(f"artifacts/integrate.txt", "a") as f:
        f.write(f"Process\t exec time for n_tasks: {n_tasks}\t res: {processes_time:.2f} sec\n\n")

    assert os.path.exists(f"artifacts/integrate.txt")
