import random
import string



INIT_ADDRESS = 0x1
WRITING_PATTERN_KEY = "writing_pattern"
MEMORY_WRITE_KEY = "memory_write"
FRAME_SIZE = 8


def compare_by_end_time(memory_write):
    return memory_write.End_time


def generate_random_data(size: int):
    return ''.join(random.choice(string.digits) for _ in range(size))
