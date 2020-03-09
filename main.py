import logging
import signal
import time

from DroneInfo import DroneInfo
from control.DroneControl import DroneControl
from control.DronePositionControl import DronePositionControl
from vision.ImageSegmentation import ImageSegmentation


class MainClass:
    def __init__(self):
        self.running = False
        self.drone = DroneControl()
        self.drone_controller = DronePositionControl()
        self.image_segmentation = ImageSegmentation()
        self.main_window = None
        self.task_period = 0.05  # seconds
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.running = True
        self.logger.info("Started System")
        self.run()

    def run(self):
        while self.running:
            image = self.drone.get_next_frame()
            info = self.image_segmentation.extract_information(image)
            # TODO: use info to complete drone_info
            drone_info = DroneInfo()
            control = self.drone_controller.compute_drone_commands(drone_info)
            # TODO: something like self.drone.send_commands(control) - 3D control
            # self.main_window.update(drone_info, image)
            time.sleep(self.task_period)

    def stop(self):
        self.running = False
        self.logger.info("Stopped System")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - [%(name)s] %(levelname)s: %(message)s")
    main = MainClass()
    signal.signal(signal.SIGINT, lambda sig, frame: main.stop())
    main.start()
