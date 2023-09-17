from typing import List
from MemoryWrite import MemoryWrite
from Utils import compare_by_end_time


class WritingPattern:
    def __init__(self, writing_pattern_dict: dict):
        self.memory_writes: List[MemoryWrite] = []
        for memory_write in writing_pattern_dict.values():
            new_memory_write: MemoryWrite = MemoryWrite(**memory_write)
            self._add_memory_write(new_memory_write)
        self.memory_writes = sorted(self.memory_writes, key=compare_by_end_time)  # Sort memory writes for each writing pattern by end time


    def _add_memory_write(self, memory_write: MemoryWrite):
        # TODO: add checks for duration/size/addresses out of bounds
        self.memory_writes.append(memory_write)

    def get_pattern(self) -> List[MemoryWrite]:
        return self.memory_writes

    def write_to_file(self, f):
        for memory_write in self.memory_writes:
            memory_write.write_to_file(f)
