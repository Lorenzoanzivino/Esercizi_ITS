from flask import Flask, jsonify, request, url_for
from ..models.security_camera import SecurityCamera
from ..models.smart_bulb import SmartBulb
from ..models.iot_hub import IoTHub

app = Flask(__name__)
iot_hub = IoTHub()

# Dispositivi di esempio
iot_hub.add(
    SmartBulb(
        serial_number="SN-101",
        brand="Philips",
        room="Living Room",
        installation_year=2022,
        status="online",
        brightness_lumens=800,
        color_capability=True,
    )
)
iot_hub.add(
    SecurityCamera(
        serial_number="SN-3e67",
        brand="Arlo",
        room="Living Room",
        installation_year=2022,
        status="online",
        resolution="1080p",
        night_vision=True,
    )
)


# --- ROUTE ---
@app.route("/")
def home():
    return jsonify(
        {
            "message": "Smart Home Hub API",
            "links": {
                "devices_list": url_for("devices_list"),
                "device_sample": url_for("get_device", serial_number="SN-101"),
                "estimate_sample": url_for(
                    "device_diagnostic", serial_number="SN-101", factor=1.0
                ),
            },
        }
    )


@app.route("/devices")
def devices_list():
    return jsonify(iot_hub.list_all())


@app.route("/devices/<serial_number>")
def get_device(serial_number):
    device = iot_hub.get(serial_number)
    if device is not None:
        return jsonify(device.info()), 200
    return jsonify({"error": f"Device {serial_number} not found"}), 404


@app.route("/devices/<serial_number>/diagnostic/<float:factor>")
def device_diagnostic(serial_number, factor):
    device = iot_hub.get(serial_number)
    if device is not None:
        return (
            jsonify(
                {
                    "serial_number": device.serial_number,
                    "device_type": device.device_type(),
                    "factor": factor,
                    "diagnostic_seconds": device.diagnostics_time(factor),
                }
            ),
            200,
        )
    return jsonify({"error": f"Device {serial_number} not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
