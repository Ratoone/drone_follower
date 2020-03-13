from DroneInfo import DroneInfo
import numpy as np

from control.DroneControl import DroneControl


class MainWindow:
    def __init__(self, drone: DroneControl = None):
        self.drone = drone
        # TODO: do the design of the UI (QT Creator with PySide2 works nice) and load it here
        pass

    def show_window(self):
        # TODO: show the UI
        pass

    def update_ui(self, drone_info: DroneInfo, image: np.ndarray):
        # TODO: update the UI with the information provided
        pass

    # TODO: add callbacks to the buttons related to the drone
