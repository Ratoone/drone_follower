from DroneInfo import DroneInfo
from vision.Preprocessing import Preprocessing
import numpy as np


class ImageSegmentation:
    """
    This class is responsible for extracting information from an image. The required info is
    the position of the drone w.r.t. the walls and the distance to the person in front (if it exists)
    """

    def __init__(self):
        self.preprocessing = Preprocessing()
        # TODO: add whatever parameters or stuff needed here

    def extract_information(self, image: np.ndarray) -> DroneInfo:
        filtered_image = self.preprocessing.process_image(image)
        # TODO: do whatever needed for image segmentation and return the required information
        return DroneInfo()

    # TODO: add methods for image segmentation
