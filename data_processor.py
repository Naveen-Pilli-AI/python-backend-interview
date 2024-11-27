import time
import json
from collections import deque

class DataProcessor:
    def __init__(self, window_size=5):
        self.data_window = deque(maxlen=window_size)

    def calculate_moving_average(self, data_point):
        self.data_window.append(data_point)
        averages = {key: sum(d[key] for d in self.data_window) / len(self.data_window) for key in data_point if isinstance(data_point[key], (int, float))}
        return {**data_point, **{"moving_averages": averages}}

def read_mock_data():
    # Replace this with actual file reading or API fetching
    with open("mock_data.json", "r") as f:
        return json.load(f)

def main():
    processor = DataProcessor()
    while True:
        data = read_mock_data()
        transformed_data = [processor.calculate_moving_average(data_point) for data_point in data]
        print(json.dumps(transformed_data, indent=4))
        time.sleep(10)

if __name__ == "__main__":
    main()
