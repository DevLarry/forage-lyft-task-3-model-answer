from tire.tire import Tire
from utils import add_years_to_date


class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        return not all([True if x >= .9 else False for x in self.sensors])