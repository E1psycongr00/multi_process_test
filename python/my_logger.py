import logging
import psutil


logger = logging.getLogger("main_logger")
logger.setLevel(logging.INFO)
cpu_clock = psutil.cpu_freq().current
cpu_count = psutil.cpu_count()
formatter = logging.Formatter(f"%(asctime)s:%(levelname)s:%(message)s [CPU Clock: {cpu_clock}Hz, CPU Core: {cpu_count}]")

file_handler = logging.FileHandler("logs/main.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


