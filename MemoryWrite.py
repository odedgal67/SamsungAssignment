import dataclasses
import struct
from typing import List

from Utils import generate_random_data, FRAME_SIZE


@dataclasses.dataclass
class MemoryWrite:
    Start_time: int
    Duration: int
    Start_address: hex
    N: int
    Data: List[str] = None
    End_time: float = None

    def __post_init__(self):
        if self.End_time is None:
            self.End_time = self.Start_time + self.Duration
        self.Data = []
        for i in range(self.N):
            self.Data.append(generate_random_data(FRAME_SIZE))

    def write_to_file(self, f):
        for i, frame in enumerate(self.Data):
            address = self.Start_address + i * FRAME_SIZE
            duration = int(self.Duration / self.N)
            f.write(struct.pack('II', address, duration) + frame.encode('utf-8'))  # TODO: fix writing format
