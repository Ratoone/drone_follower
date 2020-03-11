class DroneControl:
    def __init__(self, drone_ip="192.168.1.1"):
        self.drone_ip = drone_ip

    def connect(self):
        # TODO: connect with the drone
        pass

    # TODO: add methods for go up, down, left, right, strafe, etc

    # TODO: add methods for drone feedback: get altitude, get something, etc

    def start_streaming(self):
        pass

    def stop_streaming(self):
        pass

    def get_next_frame(self):
        # TODO: returns the next frame in the stream, non blocking
        pass
