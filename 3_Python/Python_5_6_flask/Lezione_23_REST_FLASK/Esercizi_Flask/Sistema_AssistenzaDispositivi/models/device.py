from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str):
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self):
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        pass

    @abstractmethod
    def repair_complexity(self) -> int:
        pass

    def info(self):
        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status
        }

    def estimated_total_time(self, factor: float = 1.0) -> int:
        total = int(self.base_diagnosis_time() * factor + self.repair_complexity() * 30)
        return total
