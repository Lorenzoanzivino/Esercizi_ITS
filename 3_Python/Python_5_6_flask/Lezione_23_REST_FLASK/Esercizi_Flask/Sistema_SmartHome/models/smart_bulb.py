# Lampadina intelligente

from .smart_device import SmartDevice


class SmartBulb(SmartDevice):
    brightness_lumens: int
    color_capability: bool

    def __init__(
        self,
        serial_number,
        brand,
        room,
        installation_year,
        status,
        brightness_lumens,
        color_capability,
    ):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self):
        return "bulb"

    def energy_consumption(self):
        return 9

    def connection_quality(self):
        return 2

    def info(self):
        data = super.info()
        data.update(
            {
                "brightness_lumens": self.brightness_lumens,
                "color_capability": self.color_capability,
            }
        )
        return data
