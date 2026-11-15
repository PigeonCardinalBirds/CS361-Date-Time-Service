import requests

url = "http://127.0.0.1:5000/calculate"

test_cases = [
    {"deadline": "2026-12-01"},  # Upcoming
    {"deadline": "2026-11-01"},  # Overdue
    {"deadline": "invalid-date"}  # Invalid input
]

for test in test_cases:
    response = requests.post(url, json=test)

    print("\nRequest:", test)
    print("HTTP Status:", response.status_code)
    print("Response:", response.json())
