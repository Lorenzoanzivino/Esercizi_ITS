# Astratta
from abc import ABC, abstractmethod


class SmartDevice(ABC):

    serial_number: str
    brand: str
    room: str
    installation_year: int
    status: str  # online, offline, updating, error

    def __init__(self, serial_number, brand, room, installation_year, status) -> None:
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> float | int:
        pass

    @abstractmethod
    def energy_consumption(self) -> float | int:
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        pass

    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            # più eventuali campi specifici delle sottoclassi
        }

    def diagnostic_time(self, factor: float = 1.0) -> float:
        formula = (self.energy_consumption() * factor) + self.connection_quality()
        return formula
