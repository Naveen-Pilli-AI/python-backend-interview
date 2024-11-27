import json

def analyze_data(data):
    if not data:
        return {"error": "Empty data list"}

    values = [d["value"] for d in data]
    avg_value = sum(values) / len(values)
    max_value = max(values)
    min_value = min(values)

    results = {
        "average": avg_value,
        "maximum": max_value,
        "minimum": min_value,
        "anomalies": [d for d in data if abs(d["value"] - avg_value) > 0.2 * avg_value],
    }
    return results

# Example usage
if __name__ == "__main__":
    sample_data = [
        {"timestamp": "2024-11-27T10:00:00Z", "value": 100},
        {"timestamp": "2024-11-27T10:10:00Z", "value": 80},
        {"timestamp": "2024-11-27T10:20:00Z", "value": 120},
        {"timestamp": "2024-11-27T10:30:00Z", "value": 110},
        {"timestamp": "2024-11-27T10:40:00Z", "value": 130},
    ]
    print(json.dumps(analyze_data(sample_data), indent=4))
