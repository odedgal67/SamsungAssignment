import dataclasses
import os
import secrets
from os import path

import yaml

INIT_ADDRESS = 0x1
WRITING_PATTERN_KEY = "writing_pattern"
MEMORY_WRITE_KEY = "memory_write"
FRAME_SIZE = 4
THRESHOLD_KEY = "THRESHOLD"
DELTA_KEY = "DELTA"


def compare_by_end_time(memory_write):
    return memory_write.End_time


def generate_random_data(size: int):
    return secrets.token_bytes(size)


def log(message: str):
    with open(path.join(os.getcwd(), "test_files", "log.txt"), 'a') as f:
        f.write(message)


def read_config(config_path: path) -> dict:
    with open(config_path) as f:
        config: dict = yaml.safe_load(f)
    return config


class FrameStruct:
    pass


@dataclasses.dataclass
class FrameStruct:
    address: hex
    data: bytes


