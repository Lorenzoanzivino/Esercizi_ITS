from abc import ABC, abstractmethod


class Status:
    AVAILABLE = "available"  # Diponibile nel parcheggio
    RENTED = "rented"  # Attualmente Noleggiato
    MAINTENANCE = "maintenance"  # Manutenzione
    CLEANING = "cleaning"  # Pulizia
    RETIRED = "retired"  # Dispmesso o venduto


class Vehicle(ABC):
    def __init__(
        self,
        plate_id: str,
        model: str,
        registration_year: int,
        status: Status,
        driver_name: str = None,
    ) -> None:
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def base_cleaning_time(self):
        pass

    @abstractmethod
    def wear_level(self):
        pass

    def info(self) -> dict:
        return {
            "plate_id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        return int(self.base_cleaning_time() * factor + self.wear_level() * 15)
