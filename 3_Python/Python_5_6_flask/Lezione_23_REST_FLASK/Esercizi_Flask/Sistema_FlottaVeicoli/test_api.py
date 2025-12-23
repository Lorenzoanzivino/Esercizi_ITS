import requests
import json

# Configurazione base
BASE_URL = "http://127.0.0.1:5000"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def print_separator(title):
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)


def run_tests():
    # ---------------------------------------------------------
    # 1. TEST GET / (Home)
    # ---------------------------------------------------------
    print_separator("1. TEST GET / (Benvenuto)")
    try:
        response = requests.get(f"{BASE_URL}/", headers=HEADERS)
        print(f"Status Code: {response.status_code}")
        print("Response:", json.dumps(response.json(), indent=2))
    except requests.exceptions.ConnectionError:
        print(
            "ERRORE: Impossibile connettersi. Assicurati che main.py sia in esecuzione!"
        )
        return

    # ---------------------------------------------------------
    # 2. TEST GET /vehicles (Lista Iniziale)
    # ---------------------------------------------------------
    print_separator("2. TEST GET /vehicles (Lista Iniziale)")
    response = requests.get(f"{BASE_URL}/vehicles", headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print("Veicoli trovati:", len(response.json()))
    print(json.dumps(response.json(), indent=2))

    # ---------------------------------------------------------
    # 3. TEST POST /vehicles (Creazione Nuova Auto)
    # ---------------------------------------------------------
    print_separator("3. TEST POST /vehicles (Creazione)")

    new_car_payload = {
        "type": "car",
        "plate_id": "TEST999",
        "model": "Tesla Model 3",
        "registration_year": 2023,
        "status": "available",
        "doors": 4,
        "is_cabrio": False,
        "driver_name": None,
    }

    response = requests.post(
        f"{BASE_URL}/vehicles", headers=HEADERS, json=new_car_payload
    )
    print(f"Status Code: {response.status_code} (Atteso: 201)")
    print("Response:", response.json())

    # ---------------------------------------------------------
    # 4. TEST GET /vehicles/TEST999 (Verifica Creazione)
    # ---------------------------------------------------------
    print_separator("4. TEST GET /vehicles/<id> (Verifica)")
    response = requests.get(f"{BASE_URL}/vehicles/TEST999", headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print("Dati veicolo:", response.json())

    # ---------------------------------------------------------
    # 5. TEST PATCH /vehicles/TEST999/status (Cambio Stato)
    # ---------------------------------------------------------
    print_separator("5. TEST PATCH Status (Cambio in 'rented')")
    patch_payload = {"status": "rented"}

    response = requests.patch(
        f"{BASE_URL}/vehicles/TEST999/status", headers=HEADERS, json=patch_payload
    )
    print(f"Status Code: {response.status_code}")

    # Verifichiamo che sia cambiato davvero
    check_response = requests.get(f"{BASE_URL}/vehicles/TEST999", headers=HEADERS)
    print("Nuovo stato nel DB:", check_response.json().get("status"))

    # ---------------------------------------------------------
    # 6. TEST PUT /vehicles/TEST999 (Sostituzione Totale)
    # ---------------------------------------------------------
    print_separator("6. TEST PUT (Aggiornamento Totale - Diventa Model S)")

    update_payload = {
        "type": "car",
        "model": "Tesla Model S Plaid",  # Cambiato modello
        "registration_year": 2024,  # Cambiato anno
        "status": "maintenance",  # Cambiato status
        "doors": 4,
        "is_cabrio": False,
        "driver_name": "Elon Musk",  # Aggiunto driver
    }

    response = requests.put(
        f"{BASE_URL}/vehicles/TEST999", headers=HEADERS, json=update_payload
    )
    print(f"Status Code: {response.status_code}")
    print("Veicolo aggiornato:", response.json())

    # ---------------------------------------------------------
    # 7. TEST DELETE /vehicles/TEST999
    # ---------------------------------------------------------
    print_separator("7. TEST DELETE (Cancellazione)")
    response = requests.delete(f"{BASE_URL}/vehicles/TEST999", headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json())

    # ---------------------------------------------------------
    # 8. TEST GET /vehicles/TEST999 (Verifica 404)
    # ---------------------------------------------------------
    print_separator("8. TEST GET (Verifica Eliminazione - Atteso 404)")
    response = requests.get(f"{BASE_URL}/vehicles/TEST999", headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json())


if __name__ == "__main__":
    run_tests()
