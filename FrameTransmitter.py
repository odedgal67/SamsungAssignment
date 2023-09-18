import queue
import struct
import time
from os import path
from Utils import FrameStruct, FRAME_SIZE


class FrameTransmitter:
    def __init__(self):
        self.queue = queue.Queue()

    def read_and_transmit(self, frames_file: path):
        counter: int = 1
        with open(frames_file, 'rb') as f:
            while True:
                # Read frame
                addr = f.read(4)
                if addr is None or addr == bytes():
                    break
                addr_data = struct.unpack('I', addr)[0]
                duration = f.read(4)
                duration_data = struct.unpack('f', duration)[0]
                data = f.read(FRAME_SIZE)

                # Transmit
                print(f"Transmitting frame number {counter}")
                self.transmit_frame(addr_data, data)
                time.sleep(duration_data)
                counter = counter + 1

            print("Done transmitting")

    def transmit_frame(self, addr, data):
        frame = FrameStruct(addr, data)
        self.queue.put(frame)
