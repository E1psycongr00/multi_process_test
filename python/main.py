from my_logger import logger

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import psutil
import logging
import requests


# 복잡한 계산을 하는 함수
def cpu_bound(num):
    return sum([i * i for i in range(num * 1000)])


# I/O 작업을 하는 함수
def io_bound(url):
    responses = requests.get(url)
    if responses.status_code == 200:
        return responses.status_code
    else:
        raise Exception("error")
    


def sync(func, iterable):
    """
    주어진 함수를 동기적으로 실행하고 실행 시간을 로깅합니다.

    Parameters:
        func (callable): 실행할 함수
        iterable (iterable): 함수에 전달할 인자들을 담고 있는 iterable 객체
    """
    name = func.__name__ + " " + "sync"
    start = time.time()
    results = []
    for i in iterable:
        results.append(func(i))
    end = time.time()
    logger.info(f"{name}: {end - start:.3f} seconds")
    return results


def multi_processing(func, iterable, workers=3):
    """
    주어진 함수를 멀티 프로세싱으로 실행하고 실행 시간을 로깅합니다.

    Args:
        func (callable): 병렬로 실행할 함수.
        iterable (iterable): 함수에 전달할 인자들의 반복 가능한 객체.
        workers (int, optional): 동시에 실행할 작업자(프로세스)의 수. 기본값은 3입니다.

    """
    name = func.__name__ + " " + "multi_processing"
    with ProcessPoolExecutor(max_workers=workers) as executor:
        start = time.time()
        futures = executor.map(func, iterable)
        results = []
        for future in futures:
            results.append(future)
        end = time.time()
        logger.info(f"{name}: {end - start:.3f} seconds")


def multi_threading(func, iterable, workers=3):
    """
    주어진 함수를 멀티 쓰레딩으로 실행하고 실행 시간을 로깅합니다.

    Args:
        func (callable): 실행할 함수
        iterable (iterable): 함수에 전달할 인자들의 반복 가능한 객체
        workers (int, optional): 동시에 실행할 스레드 수 (기본값: 3)

    Returns:
        list: 함수 실행 결과들의 리스트
    """
    name = func.__name__ + " " + "multi_threading"
    with ThreadPoolExecutor(max_workers=workers) as executor:
        start = time.time()
        futures = executor.map(func, iterable)
        results = []
        for future in futures:
            results.append(future)
        end = time.time()
        logger.info(f"{name}: {end - start:.3f} seconds")


if __name__ == '__main__':
    cpu_input_list = [2000, 4000, 6000, 8000]
    io_input_list = ["https://httpbin.org/get"] * 4

    sync(cpu_bound, cpu_input_list)
    sync(io_bound, io_input_list)
    multi_processing(cpu_bound, cpu_input_list)
    multi_threading(cpu_bound, cpu_input_list)
    multi_processing(io_bound, io_input_list)
    multi_threading(io_bound, io_input_list)