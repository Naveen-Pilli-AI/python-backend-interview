# Python Backend Interview Test

This repository contains the solution to the Backend Interview Test, which consists of three tasks focused on data ingestion and processing, building a simple REST API, and performing basic data analytics.

## Table of Contents

1. [Task 1 - Data Ingestion & Processing](#task-1---data-ingestion--processing)
2. [Task 2 - Basic REST API Development](#task-2---basic-rest-api-development)
3. [Task 3 - Simple Data Analytics](#task-3---simple-data-analytics)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)

---

## Task 1 - Data Ingestion & Processing

### Description
This task involves writing a Python script that reads a continuous stream of simulated machine data (e.g., temperature, speed, and status), calculates a moving average over the last 5 readings, and outputs the transformed data as JSON.

### Implementation
The script reads data from a mock JSON file every 10 seconds, calculates the moving average for each parameter, and prints the result.

---

## Task 2 - Basic REST API Development

### Description
A simple REST API using Flask is created with two endpoints:
- **GET /data**: Returns the processed machine data as JSON.
- **POST /status**: Allows updating the machine’s job status (e.g., "STARTED", "COMPLETED").

### Implementation
- Validates the status input for the `/status` endpoint.
- Stores and manages machine status updates in memory.

---

## Task 3 - Simple Data Analytics

### Description
This task involves a Python function that reads a list of timestamps and values (e.g., machine speed) and calculates:
- Average value over the entire period
- Maximum and minimum values

**Bonus**: Detects anomalies if any value deviates by more than 20% from the average.

### Implementation
The function returns the average, maximum, and minimum values, along with any anomalies detected.

---

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Naveen-Pilli-AI/python-backend-interview.git
    cd python-backend-interview
    ```

2. **Install dependencies**:
    It's recommended to use `poetry` for managing dependencies. To install poetry:
    ```bash
    pip install poetry
    ```

    Then install the project dependencies:
    ```bash
    poetry install
    ```

---

## Usage

### Task 1 - Running Data Ingestion & Processing Script

To run the data ingestion and processing script, simply execute the following command:


python data_processor.py

### Task 2 - Running the Flask API
Start the Flask API by running:

python api.py

The API will be available at http://127.0.0.1:5000.

GET /data: Returns the processed data as JSON.
POST /status: Accepts a JSON payload to update the machine status, e.g.
{ "status": "STARTED" }

### Task 3 - Running Data Analytics

To analyze a set of data, modify the sample_data list in the analytics.py file and run:

python analytics.py
