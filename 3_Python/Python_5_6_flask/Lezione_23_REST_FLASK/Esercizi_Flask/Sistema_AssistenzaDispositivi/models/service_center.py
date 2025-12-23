class ServiceCenter:
    def __init__(self):
        self.devices = {}

    def add(self, device):
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True

    def get(self, device_id):
        return self.devices.get(device_id)

    def update(self, device_id, new_device):
        if device_id in self.devices:
            self.devices[device_id] = new_device
            return True
        return False

    def patch_status(self, device_id, new_status):
        if device_id in self.devices:
            self.devices[device_id].status = new_status.status
            return True
        return False

    def delete(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

    def list_all(self):
        return [device.info() for device in self.devices.values()]
