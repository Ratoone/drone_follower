import numpy as np


class DroneControl:
    """
    Basic methods for drone control. This will work as a wrapper over the drone's SDK.
    """

    def __init__(self, drone_ip: str = "192.168.1.1"):
        self.drone_ip = drone_ip

    def connect(self):
        """ Initialize the connection with the drone """
        # TODO: connect with the drone
        pass

    # TODO: add methods for go up, down, left, right, strafe, etc

    # TODO: add methods for drone feedback: get altitude, get something, etc

    def start_streaming(self):
        # TODO: make sure this starts a separate thread with the camera stream
        pass

    def stop_streaming(self):
        """ Stop the camera streaming thread """
        pass

    def get_next_frame(self) -> np.ndarray:
        """ Returns the next frame from the stream """
        # TODO: returns the next frame in the stream, non blocking
        pass
