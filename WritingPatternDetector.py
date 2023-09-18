import os
import queue
import time
from os import path
from typing import List

from Exceptions import SystemFailureException, InvalidConfigException
from FrameTransmitter import FrameTransmitter
from Utils import FrameStruct, log, read_config, THRESHOLD_KEY, DELTA_KEY


class WritingPatternDetector:
    def __init__(self, transmitter, config_path):
        self.transmitter: FrameTransmitter = transmitter
        self.frames: List[FrameStruct] = list()
        self.min_addr = 99999
        self.max_addr = 0
        self.config_path = config_path
        self.threshold = None
        self.delta = None
        self._read_threshold_delta()
        self.start_time = None

    def get_frames(self):
        self.start_time = time.time()
        while True:
            if self.transmitter.queue.empty():
                break
            frame: FrameStruct = self.transmitter.queue.get()
            self.frames.append(frame)
            self._detect_pattern(frame)
            self._write_to_flash(frame)

    def _detect_pattern(self, frame: FrameStruct):
        delta_time = time.time() - self.start_time
        curr_addr = frame.address

        # Update min max fields
        if curr_addr < self.min_addr:
            self.min_addr = curr_addr
        if curr_addr > self.max_addr:
            self.max_addr = curr_addr

        delta_addr = self.max_addr - self.min_addr

        if delta_time <= self.delta and delta_addr >= self.threshold:
            self._system_failure_handler()

    def _system_failure_handler(self):
        log(f"{time.time()} : System failure detected\tDELTA : {self.delta}\tTHRESHOLD : {self.threshold}")
        raise SystemFailureException(self.threshold, self.delta)

    def _write_to_flash(self, frame: FrameStruct):
        with open(path.join(os.getcwd(), "test_files", "flash.bin"), 'ab') as f:
            f.write(frame.data)

    def _read_threshold_delta(self):
        config: dict = read_config(self.config_path)
        if THRESHOLD_KEY not in config or DELTA_KEY not in config:
            raise InvalidConfigException
        self.delta = config[DELTA_KEY]
        self.threshold = config[THRESHOLD_KEY]
