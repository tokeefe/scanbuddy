import os
import sys
import psutil
import platform
from tabulate import tabulate

def print_platform_info():
    rss = psutil.virtual_memory().total / 1024**3
    swap = psutil.swap_memory().total / 1024**3
    table = [
        ['Platform', platform.platform()],
        ['CPU Arch', platform.processor()],
        ['CPU Count', os.cpu_count()],
        ['System RAM', f'{rss:.2f} GB'],
        ['System Swap', f'{swap:.2f} GB'],
        ['Python version', platform.python_version()],
        ['GIL enabled', sys._is_gil_enabled()]
    ]
    print(tabulate(table, tablefmt='simple_grid'))
