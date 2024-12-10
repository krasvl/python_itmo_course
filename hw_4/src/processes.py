import logging
import multiprocessing
import time
import codecs

def get_logger(name, log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.addHandler(handler)
    return logger

def process_a(input_queue, output_queue):
    logger_a = get_logger("process_a", "artifacts/process_a.log")
    while True:
        message = input_queue.get()
        if message == "STOP":
            output_queue.put("STOP")
            break

        lower_message = message.lower()
        time.sleep(5)

        logger_a.info(f"get: {message}\t put: {lower_message}")
        output_queue.put(lower_message)


def process_b(input_queue, output_queue):
    logger_b = get_logger("process_b", "artifacts/process_b.log")
    while True:
        message = input_queue.get()
        if message == "STOP":
            output_queue.put("STOP")
            break

        rot13_message = codecs.encode(message, 'rot_13')

        logger_b.info(f"get: {message}\t put: {rot13_message}")
        output_queue.put(rot13_message)


def process(input_to_a_queue, a_to_b_queue, b_to_output_queue):
    a_process = multiprocessing.Process(target=process_a, args=(input_to_a_queue, a_to_b_queue))
    b_process = multiprocessing.Process(target=process_b, args=(a_to_b_queue, b_to_output_queue))

    a_process.start()
    b_process.start()

    a_process.join()
    b_process.join()