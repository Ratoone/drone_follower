from vision.Preprocessing import Preprocessing


class ImageSegmentation:
    def __init__(self):
        self.preprocessing = Preprocessing()
        # TODO: add whatever parameters or stuff needed here

    def extract_information(self, image):
        filtered_image = self.preprocessing.process_image(image)
        # TODO: do whatever needed for image segmentation and return the required information
        return {}

    # TODO: add methods for image segmentation
