from models.vehicle import Vehicle


class FleetManager:
    def __init__(self):
        self.vehicles: dict = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False
        else:
            self.vehicles[vehicle.plate_id] = vehicle
            return True

    def get(self, plate_id: str) -> Vehicle:
        return self.vehicles.get(plate_id)

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id] = new_vehicle

    def patch_status(self, plate_id, new_vehicle: Vehicle) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id].status = new_vehicle.status

    def delete(self, plate_id) -> bool:
        if plate_id not in self.vehicles:
            return False
        del self.vehicles[plate_id]
        return True

    def list_all(self):
        result = []
        for vehicle in self.vehicles.values():
            result.append(vehicle.info())
        return result
