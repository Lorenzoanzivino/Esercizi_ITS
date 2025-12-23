from models.vehicle import Vehicle


class Car(Vehicle):
    def __init__(
        self,
        plate_id,
        model,
        registration_year,
        status,
        doors: int,
        is_cabrio: bool,
        driver_name=None,
    ):
        super().__init__(plate_id, model, registration_year, status, driver_name)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self):
        return "car"

    def base_cleaning_time(self):
        return 30

    def wear_level(self):
        return 1

    def info(self):
        base_data_car = super().info()

        base_data_car["doors"] = self.doors
        base_data_car["is_cabrio"] = self.is_cabrio

        return base_data_car
