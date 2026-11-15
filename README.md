# Date and Time Microservice

## Description

This microservice calculates the number of days remaining until a specified deadline.

It validates submitted dates and returns an error for invalid input.

## Communication Contract

**Communication Pipe:** REST API

**Endpoint:** `http://127.0.0.1:5000/calculate`

**Method:** POST

**Data Format:** JSON

### Requesting Data

The requesting program sends an HTTP POST request containing a deadline in YYYY-MM-DD format.

Required parameter:
- `deadline`: Date in YYYY-MM-DD format.

Example request:

```python
import requests

response = requests.post(
    "http://127.0.0.1:5000/calculate",
    json={"deadline": "2026-12-01"}
)
```

### Receiving Data

The microservice returns a JSON response containing:

- `deadline`: The submitted deadline.
- `days_remaining`: Number of days until the deadline.

Example response:

```json
{
    "deadline": "2026-12-01",
    "days_remaining": 16
}
```

The number of days is calculated using the server's current local date.

Example receiving code:

```python
data = response.json()

print(data["deadline"])
print(data["days_remaining"])
```

### Error Handling

Invalid dates return HTTP 400.

Example:

```json
{
    "error": "Invalid deadline. Use YYYY-MM-DD format."
}
```

Missing required fields also return HTTP 400.

## Running the Microservice

Install dependencies:

```bash
python -m pip install flask requests
```

Start the server:

```bash
python date_time_service.py
```

In a separate terminal, run:

```bash
python test_date_time.py
```

## UML Sequence Diagram

```mermaid
sequenceDiagram
    participant Client as Requesting Program
    participant API as Date and Time Microservice

    Client->>API: POST /calculate (deadline JSON)
    API->>API: calculate_deadline()
    API->>API: Validate deadline

    alt Valid deadline
        API->>API: Calculate days_remaining
        API-->>Client: HTTP 200 (deadline, days_remaining)
    else Invalid or missing deadline
        API-->>Client: HTTP 400 (error message)
    end
```