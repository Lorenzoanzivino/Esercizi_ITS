# Telecamera di sicurezza

from smart_device import SmartDevice


class SecurityCamera(SmartDevice):
    def __init__(
        self,
        serial_number,
        brand,
        room,
        installation_year,
        status,
        resolution,
        night_vision,
    ):
        super().__init__(serial_number, brand, room, installation_year, status)

        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self):
        return "camera"

    def energy_consumption(self):
        return 50

    def connection_quality(self):
        return 8

    def info(self):
        data = super.info()
        data.update(
            {
                "resolution": self.resolution,
                "night_vision": self.night_vision,
            }
        )

        return data
