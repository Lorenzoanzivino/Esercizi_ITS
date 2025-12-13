import requests
import json

BASE_URL = "http://localhost:5000"
headers = {"Content-type": "application/json", "Accept": "application/json"}

def print_response(resp):
    print(resp.status_code, resp.json())

if __name__ == "__main__":
    # GET /
    resp = requests.get(f"{BASE_URL}/", headers=headers)
    print_response(resp)

    # GET /devices
    resp = requests.get(f"{BASE_URL}/devices", headers=headers)
    print_response(resp)

    # POST nuovo smartphone
    new_device = {
        "type": "smartphone",
        "id": "d3",
        "model": "Galaxy S21",
        "customer_name": "Mario Rossi",
        "purchase_year": 2021,
        "status": "received",
        "has_protective_case": True,
        "storage_gb": 128
    }
    resp = requests.post(f"{BASE_URL}/devices", headers=headers, data=json.dumps(new_device))
    print_response(resp)

    # GET /devices/d3
    resp = requests.get(f"{BASE_URL}/devices/d3", headers=headers)
    print_response(resp)

    # PATCH stato
    resp = requests.patch(f"{BASE_URL}/devices/d3/status", headers=headers, data=json.dumps({"status": "repairing"}))
    print_response(resp)

    # PUT dispositivo
    updated_device = new_device.copy()
    updated_device["model"] = "Galaxy S22"
    resp = requests.put(f"{BASE_URL}/devices/d3", headers=headers, data=json.dumps(updated_device))
    print_response(resp)

    # DELETE dispositivo
    resp = requests.delete(f"{BASE_URL}/devices/d3", headers=headers)
    print_response(resp)

    # GET dispositivo dopo DELETE
    resp = requests.get(f"{BASE_URL}/devices/d3", headers=headers)
    print_response(resp)
