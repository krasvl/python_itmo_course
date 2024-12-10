import multiprocessing
import os
import pytest
import time
from processes import process

@pytest.mark.parametrize("text", [
    "TEST1\nTEST2\nSTOP",
    "TEST1\nTEST2\nTEST3\nTEST4\nSTOP",
    "TeSt1\ntEsT2\nSTOP",
])
def test_process_communication(text):
    os.makedirs("artifacts", exist_ok=True)

    input_to_a_queue = multiprocessing.Queue()
    a_to_b_queue = multiprocessing.Queue()
    b_to_output_queue = multiprocessing.Queue()

    for line in text.splitlines():
        input_to_a_queue.put(line)

    process(input_to_a_queue, a_to_b_queue, b_to_output_queue)

    with open("artifacts/input_to_a.txt", "a") as f:
        f.write(text + "\n")

    with open("artifacts/b_to_output.txt", "a") as f:
        while not b_to_output_queue.empty():
            f.write(b_to_output_queue.get() + "\n")

    assert os.path.exists("artifacts/input_to_a.txt")
    assert os.path.exists("artifacts/b_to_output.txt")