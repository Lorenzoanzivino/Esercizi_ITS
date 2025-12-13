from flask import Flask, jsonify, request, url_for
from models.smartphone import Smartphone
from models.laptop import Laptop
from models.service_center import ServiceCenter

app = Flask(__name__)
service_center = ServiceCenter()

# Dispositivi di esempio
service_center.add(Smartphone("d1", "iPhone 13", "Lorenzo", 2022, "received", True, 128))
service_center.add(Laptop("d2", "ThinkPad X1", "Giulia", 2021, "diagnosing", True, 15.6))

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Service Center API",
        "links": {
            "list_devices": url_for('list_devices', _external=True),
            "sample_device": url_for('get_device', device_id='d1', _external=True),
            "sample_estimate": url_for('estimate_device', device_id='d1', factor=1.5, _external=True)
        }
    })

@app.route("/devices", methods=["GET"])
def list_devices():
    return jsonify(service_center.list_all())

@app.route("/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    device = service_center.get(device_id)
    if device:
        return jsonify(device.info())
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices/<device_id>/estimate/<float:factor>", methods=["GET"])
def estimate_device(device_id, factor):
    device = service_center.get(device_id)
    if device:
        return jsonify({
            "id": device.id,
            "device_type": device.device_type(),
            "factor": factor,
            "estimated_total_minutes": device.estimated_total_time(factor)
        })
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices", methods=["POST"])
def add_device():
    data = request.get_json()
    if not data or "type" not in data or "id" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        if data["type"] == "smartphone":
            device = Smartphone(
                data["id"], data["model"], data["customer_name"], data["purchase_year"], 
                data["status"], data["has_protective_case"], data["storage_gb"]
            )
        elif data["type"] == "laptop":
            device = Laptop(
                data["id"], data["model"], data["customer_name"], data["purchase_year"], 
                data["status"], data["has_dedicated_gpu"], data["screen_size_inches"]
            )
        else:
            return jsonify({"error": "Invalid device type"}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing field {e}"}), 400

    if service_center.add(device):
        return jsonify(device.info()), 201
    return jsonify({"error": "Device ID already exists"}), 400

@app.route("/devices/<device_id>", methods=["PUT"])
def put_device(device_id):
    data = request.get_json()
    if not data or "type" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        if data["type"] == "smartphone":
            new_device = Smartphone(
                device_id, data["model"], data["customer_name"], data["purchase_year"], 
                data["status"], data["has_protective_case"], data["storage_gb"]
            )
        elif data["type"] == "laptop":
            new_device = Laptop(
                device_id, data["model"], data["customer_name"], data["purchase_year"], 
                data["status"], data["has_dedicated_gpu"], data["screen_size_inches"]
            )
        else:
            return jsonify({"error": "Invalid device type"}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing field {e}"}), 400

    if service_center.update(device_id, new_device):
        return jsonify(new_device.info())
    else:
        # opzionale: crea nuovo se non esiste
        service_center.add(new_device)
        return jsonify(new_device.info()), 201

@app.route("/devices/<device_id>/status", methods=["PATCH"])
def patch_device_status(device_id):
    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "Missing status field"}), 400
    if service_center.patch_status(device_id, data["status"]):
        return jsonify(service_center.get(device_id).info())
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices/<device_id>", methods=["DELETE"])
def delete_device(device_id):
    if service_center.delete(device_id):
        return jsonify({"deleted": True, "id": device_id})
    return jsonify({"error": "Device not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
