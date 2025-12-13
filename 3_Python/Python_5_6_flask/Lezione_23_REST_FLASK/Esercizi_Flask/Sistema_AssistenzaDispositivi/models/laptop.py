from .device import Device

class Laptop(Device):
    def __init__(self, id, model, customer_name, purchase_year, status, has_dedicated_gpu: bool, screen_size_inches: float):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self):
        return "laptop"

    def base_diagnosis_time(self):
        return 40

    def repair_complexity(self):
        return 4

    def info(self):
        data = super().info()
        data.update({
            "has_dedicated_gpu": self.has_dedicated_gpu,
            "screen_size_inches": self.screen_size_inches
        })
        return data
