import requests

BASE_URL = "http://127.0.0.1:5000"

# Test GET /data
response = requests.get(f"{BASE_URL}/data")
print("GET /data Response:", response.json())

# Test POST /status with valid data
valid_status = {"status": "STARTED"}
response = requests.post(f"{BASE_URL}/status", json=valid_status)
print("POST /status Response (valid):", response.json())

# Test POST /status with invalid data
invalid_status = {"status": "INVALID"}
response = requests.post(f"{BASE_URL}/status", json=invalid_status)
print("POST /status Response (invalid):", response.json())
