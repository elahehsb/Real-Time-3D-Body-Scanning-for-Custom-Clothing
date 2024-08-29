import cv2
import numpy as np

class DataAcquisition:
    def __init__(self, scanner_device):
        self.scanner = scanner_device

    def capture_body_data(self):
        depth_data = self.scanner.capture_depth()
        rgb_data = self.scanner.capture_rgb()
        return depth_data, rgb_data

    def release_device(self):
        self.scanner.release()

if __name__ == "__main__":
    # Example of using a mock scanner
    class MockScanner:
        def capture_depth(self):
            return np.random.rand(480, 640)

        def capture_rgb(self):
            return np.zeros((480, 640, 3), dtype=np.uint8)

        def release(self):
            print("Scanner released")

    scanner = MockScanner()
    acquisition = DataAcquisition(scanner)
    depth, rgb = acquisition.capture_body_data()
    acquisition.release_device()

    print("Captured Depth Data:", depth.shape)
    print("Captured RGB Data:", rgb.shape)
