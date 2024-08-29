import cv2
import numpy as np

class ImageProcessing:
    def __init__(self, rgb_data, depth_data):
        self.rgb_data = rgb_data
        self.depth_data = depth_data

    def extract_features(self):
        # Example: Apply edge detection as a feature extraction method
        edges = cv2.Canny(self.rgb_data, 100, 200)
        return edges

    def align_depth_to_rgb(self):
        # Example: Simple alignment by resizing (mock implementation)
        aligned_depth = cv2.resize(self.depth_data, (self.rgb_data.shape[1], self.rgb_data.shape[0]))
        return aligned_depth

if __name__ == "__main__":
    mock_rgb = np.zeros((480, 640, 3), dtype=np.uint8)
    mock_depth = np.random.rand(480, 640)

    processor = ImageProcessing(mock_rgb, mock_depth)
    features = processor.extract_features()
    aligned_depth = processor.align_depth_to_rgb()

    print("Extracted Features Shape:", features.shape)
    print("Aligned Depth Shape:", aligned_depth.shape)
