from flask import Flask, request, jsonify, url_for
from models.vehicle import Status
from models.car import Car
from models.van import Van
from models.fleetManager import FleetManager

app = Flask(__name__)

fleetManager = FleetManager()

# Creiamo una Macchina
# Ordine: targa, modello, anno, status, porte, is_cabrio, (driver_name opzionale)
car_1 = Car("AB123CD", "Fiat Panda", 2022, Status.AVAILABLE, 5, False)

# Creiamo un Furgone
# Ordine: targa, modello, anno, status, max_load, patente_speciale, (driver_name)
van_1 = Van("XY987ZW", "Ford Transit", 2020, Status.RENTED, 1000, False, "Mario Rossi")

# Aggiungiamoli al "database"
fleetManager.add(car_1)
fleetManager.add(van_1)


@app.route("/", methods=["GET"])
def home():
    # Qui devi costruire il dizionario usando url_for
    # Ricorda: url_for prende come primo argomento il NOME DELLA FUNZIONE target
    data = {
        "message": "Welcome to Rent Center API",
        "links": {
            "vehicles_list": url_for("list_vehicles"),
            # Nota come passiamo i parametri dinamici (plate_id)
            "vehicle_sample": url_for("get_vehicle", plate_id="HA014AS"),
            "estimate_sample": url_for("get_prep_time", plate_id="HA014AS", factor=2.0),
        },
    }
    return jsonify(data)


@app.route("/vehicles", methods=["GET"])
def list_vehicles():
    return jsonify(fleetManager.list_all())


@app.route("/vehicles/<plate_id>", methods=["GET"])
def get_vehicle(plate_id):
    vehicle = fleetManager.get(plate_id)
    if vehicle:
        return jsonify(vehicle.info())
    return jsonify({"error": "vehicle not found"}), 404


@app.route("/vehicles/<plate_id>/prep-time/<factor>", methods=["GET"])
def get_prep_time(plate_id, factor):
    vehicle = fleetManager.get(plate_id)
    if vehicle:
        return jsonify(
            {
                "id": vehicle.plate_id,
                "vehicle_type": vehicle.vehicle_type(),
                "factor": factor,
                "estimated_sample": vehicle.estimated_sample(factor),
            }
        )
    return jsonify({"error": "vehicle not found"}), 404


@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    data = request.get_json()

    # 1. Controllo preliminare
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    vehicle_type = data.get("type")  # "car" o "van"

    # Variabile per il nuovo veicolo
    new_vehicle = None

    try:
        # 2. Logica di creazione in base al tipo
        if vehicle_type == "car":
            new_vehicle = Car(
                plate_id=data["plate_id"],
                model=data["model"],
                registration_year=data["registration_year"],
                status=data["status"],
                driver_name=data.get("driver_name"),  # Opzionale (usa .get)
                doors=data["doors"],
                is_cabrio=data["is_cabrio"],
            )

        elif vehicle_type == "van":
            new_vehicle = Van(
                plate_id=data["plate_id"],
                model=data["model"],
                registration_year=data["registration_year"],
                status=data["status"],
                driver_name=data.get("driver_name"),  # Opzionale
                max_load_kg=data["max_load_kg"],
                require_special_license=data["require_special_license"],
            )

        else:
            return (
                jsonify({"error": "Unknown vehicle type (must be 'car' or 'van')"}),
                400,
            )

        # 3. Aggiunta al manager
        success = fleetManager.add(new_vehicle)

        if success:
            return jsonify(new_vehicle.info()), 201
        else:
            return (
                jsonify({"error": "Vehicle with this plate_id already exists"}),
                400,
            )  # O 409 Conflict

    except KeyError as e:
        # Se mancano chiavi nel JSON (es. manca "model")
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400


@app.route("/vehicles/<plate_id>", methods=["PUT"])
def update_vehicle(plate_id):
    # Verifichiamo prima se il veicolo esiste per restituire 404 se necessario
    if not fleetManager.get(plate_id):
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    vehicle_type = data.get("type")
    new_vehicle = None

    try:
        # Logica di creazione (identica alla POST)
        if vehicle_type == "car":
            new_vehicle = Car(
                plate_id=plate_id,  # Usiamo l'ID dell'URL per sicurezza
                model=data["model"],
                registration_year=data["registration_year"],
                status=data["status"],
                driver_name=data.get("driver_name"),
                doors=data["doors"],
                is_cabrio=data["is_cabrio"],
            )
        elif vehicle_type == "van":
            new_vehicle = Van(
                plate_id=plate_id,
                model=data["model"],
                registration_year=data["registration_year"],
                status=data["status"],
                driver_name=data.get("driver_name"),
                max_load_kg=data["max_load_kg"],
                require_special_license=data["require_special_license"],
            )
        else:
            return jsonify({"error": "Unknown vehicle type"}), 400

        # Effettuiamo l'update
        fleetManager.update(plate_id, new_vehicle)

        # Restituiamo il veicolo aggiornato
        return jsonify(new_vehicle.info()), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400


@app.route("/vehicles/<plate_id>/status", methods=["PATCH"])
def patch_vehicle_status(plate_id):
    # 1. Verifica esistenza
    existing_vehicle = fleetManager.get(plate_id)
    if not existing_vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.get_json()
    new_status = data.get("status")

    if not new_status:
        return jsonify({"error": "Missing 'status' field"}), 400

    # 2. Trucco: Creiamo un oggetto semplice per passare lo status
    # Usiamo una classe generica o riusiamo una Car "finta" solo per trasportare lo status
    # Dato che Python è flessibile, modifichiamo lo status dell'oggetto esistente
    # creando un oggetto temporaneo dello stesso tipo.

    # Per semplicità e rispettare la firma di fleetManager.patch_status(id, new_vehicle):
    # Creiamo una copia "dummy" del veicolo esistente con il nuovo status
    dummy_vehicle = existing_vehicle
    dummy_vehicle.status = new_status

    fleetManager.patch_status(plate_id, dummy_vehicle)

    return jsonify({"message": "Status updated", "new_status": new_status}), 200


@app.route("/vehicles/<plate_id>", methods=["DELETE"])
def delete_vehicle(plate_id):
    success = fleetManager.delete(plate_id)

    if success:
        return jsonify({"deleted": True, "id": plate_id}), 200
    else:
        return jsonify({"error": "Vehicle not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
