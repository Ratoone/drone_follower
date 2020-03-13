class DroneInfo:
    """
    Data structure containing information about the drone and the drone's
    surroundings
    """
    def __init__(self, altitude: float = 0, orientation: float = 0, hall_width: float = 0, horizontal_position: float = 0):
        self.altitude = altitude
        self.orientation = orientation
        self.hall_width = hall_width
        self.horizontal_position = horizontal_position
