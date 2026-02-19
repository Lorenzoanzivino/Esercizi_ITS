# Sistema di gestione di dispositivi intelligenti

from smart_device import SmartDevice


class IoTHub:
    devices: dict

    def __init__(self):
        self.devices = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number not in self.devices:
            self.devices[device.serial_number] = device
            return True
        return False

    def get(self, serial_number: str) -> SmartDevice | None:
        if serial_number in self.devices:
            return self.devices.get(serial_number)
        return None

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        if serial_number in self.devices:
            self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        if serial_number in self.devices:
            self.devices[serial_number].status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number in self.devices:
            del self.devices[serial_number]
            print(
                f"Eliminzazione del dispositivo: {serial_number} è andata a buon fine"
            )
            return True
        print(f"Il dispositivo: {serial_number} Non esiste")
        return False

    def list_all(self) -> list[dict[str, float | int | str]]:
        result = []
        for device in self.devices.values():
            result.append(device.info())
        return result
