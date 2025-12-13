from .device import Device

class Smartphone(Device):
    def __init__(self, id, model, customer_name, purchase_year, status, has_protective_case: bool, storage_gb: int):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self):
        return "smartphone"

    def base_diagnosis_time(self):
        return 20

    def repair_complexity(self):
        return 2

    def info(self):
        data = super().info()
        data.update({
            "has_protective_case": self.has_protective_case,
            "storage_gb": self.storage_gb
        })
        return data
