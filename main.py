from DroneInfo import DroneInfo
from control.DroneControl import DroneControl
from vision.ImageSegmentation import ImageSegmentation


class MainClass:
    def __init__(self):
        self.running = False
        self.drone = DroneControl()
        self.image_segmentation = ImageSegmentation()
        self.main_window = None
        self.time_sample = 0.05 # seconds

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            image = self.drone.get_next_frame()
            info = self.image_segmentation.extract_information(image)
            # TODO: use info to complete drone_info
            drone_info = DroneInfo()
            


if __name__ == "__main__":
    MainClass().start()
