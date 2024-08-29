import numpy as np

class BodyReconstruction:
    def __init__(self, features, aligned_depth):
        self.features = features
        self.aligned_depth = aligned_depth

    def reconstruct_body(self):
        # Example: Simple mock 3D reconstruction combining features and depth data
        vertices = np.hstack((self.features.flatten().reshape(-1, 1), self.aligned_depth.flatten().reshape(-1, 1)))
        return vertices

if __name__ == "__main__":
    mock_features = np.random.rand(480, 640)
    mock_aligned_depth = np.random.rand(480, 640)
    
    reconstructor = BodyReconstruction(mock_features, mock_aligned_depth)
    vertices = reconstructor.reconstruct_body()

    print("Reconstructed Vertices:", vertices.shape)
