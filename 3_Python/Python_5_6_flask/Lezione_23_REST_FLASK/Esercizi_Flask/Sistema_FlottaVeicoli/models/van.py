from models.vehicle import Vehicle


class Van(Vehicle):
    def __init__(
        self,
        plate_id,
        model,
        registration_year,
        status,
        max_load_kg: int,
        require_special_license: bool,
        driver_name=None,
    ):
        super().__init__(plate_id, model, registration_year, status, driver_name)

        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self):
        return "van"

    def base_cleaning_time(self):
        return 60

    def wear_level(self):
        return 4

    def info(self):
        base_data_van = super().info()

        base_data_van["max_load_kg"] = self.max_load_kg
        base_data_van["require_special_license"] = self.require_special_license

        return base_data_van
