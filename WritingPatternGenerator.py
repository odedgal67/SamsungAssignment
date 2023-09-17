import os
from os import path
from typing import List
import yaml

from MemoryWrite import MemoryWrite
from Utils import generate_random_data
from WritingPattern import WritingPattern


class WritingPatternGenerator:
    def __init__(self):
        self.writing_patterns: List[WritingPattern] = []

    def generate_bin(self, config_path: path, output_path: path):
        config: dict = self._read_config(config_path)
        for key, value in config.items():
            if key in ["THRESHOLD", "DELTA"]:
                continue
            new_writing_pattern: WritingPattern = WritingPattern(value)
            self.writing_patterns.append(new_writing_pattern)
        with open(output_path, 'wb') as f:
            for writing_pattern in self.writing_patterns:
                writing_pattern.write_to_file(f)

    def _read_config(self, config_path: path) -> dict:
        with open(config_path) as f:
            config: dict = yaml.safe_load(f)
        return config

    def _get_all_memory_writes(self) -> List[MemoryWrite]:
        for writing_pattern in self.writing_patterns.values():
            raise NotImplemented


if __name__ == '__main__':
    pattern_gen: WritingPatternGenerator = WritingPatternGenerator()
    config_path: path = path.join(os.getcwd(), "test_files", "config.yaml")
    pattern_gen.generate_bin(config_path, path.join(os.getcwd(), "test_files", "output.bin"))

