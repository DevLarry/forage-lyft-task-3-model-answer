from serviceable import Serviceable
from tire.carrigan_tire import CarriganTire


class Car(Serviceable):
    def __init__(self, engine, battery, tire = None):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        if tire is None:
            tire = CarriganTire([0, 0, 0, 0])

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
