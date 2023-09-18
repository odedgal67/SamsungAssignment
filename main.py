import os
from os import path

from FrameTransmitter import FrameTransmitter
from WritingPatternDetector import WritingPatternDetector
from WritingPatternGenerator.WritingPatternGenerator import WritingPatternGenerator

if __name__ == '__main__':

    # Generate bin file from config
    pattern_gen: WritingPatternGenerator = WritingPatternGenerator()
    config_path: path = path.join(os.getcwd(), "test_files", "config.yaml")
    frames_bin_file_path: path = path.join(os.getcwd(), "test_files", "FRAMES.bin")

    pattern_gen.generate_bin(config_path, frames_bin_file_path)

    # Transmit frames from frames transmitter to pattern detector
    frames_transmitter: FrameTransmitter = FrameTransmitter()
    writing_pattern_detector: WritingPatternDetector = WritingPatternDetector(frames_transmitter, config_path)

    frames_transmitter.read_and_transmit(frames_bin_file_path)
    writing_pattern_detector.get_frames()

