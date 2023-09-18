import os
from os import path
from typing import List
from MemoryWrite import MemoryWrite
from Utils import generate_random_data, read_config, THRESHOLD_KEY, DELTA_KEY
from WritingPattern import WritingPattern


class WritingPatternGenerator:
    def __init__(self):
        self.writing_patterns: List[WritingPattern] = []

    def generate_bin(self, config_path: path, output_path: path):
        config: dict = read_config(config_path)
        for key, value in config.items():
            if key in [THRESHOLD_KEY, DELTA_KEY]:
                continue
            new_writing_pattern: WritingPattern = WritingPattern(value)
            self.writing_patterns.append(new_writing_pattern)
        with open(output_path, 'wb') as f:
            for writing_pattern in self.writing_patterns:
                writing_pattern.write_to_file(f)
