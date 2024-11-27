from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
machine_status = {"status": "IDLE"}
processed_data = []
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API. Use /data or /status endpoints."})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(processed_data)

@app.route('/status', methods=['POST'])
def update_status():
    valid_statuses = {"STARTED", "COMPLETED", "IDLE"}
    data = request.json
    if "status" not in data or data["status"] not in valid_statuses:
        return jsonify({"error": "Invalid status"}), 400
    machine_status["status"] = data["status"]
    return jsonify({"message": "Status updated", "status": machine_status["status"]})

if __name__ == "__main__":
    app.run(debug=True)
