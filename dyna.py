import requests
import json
import uuid

url = "https://openapi.api.govee.com/router/api/v1/device/scenes" #pre-set scenes
#url = "https://openapi.api.govee.com/router/api/v1/device/diy-scenes" #diy scenes
api_key = "6dc03b20-0ea0-4fde-a9c1-b245e3342864"
uid = uuid.uuid4()

headers = {
    "Content-Type": "application/json",
    "Govee-API-Key": api_key,
}

params = {
    "requestId": str(uid),  # Use the generated UUID here
    "payload": {
        "sku": "H6061",
        "device": "F0:2D:D1:32:38:30:4C:5C"
    }
}

response = requests.post(url, json=params, headers = headers)
try:
    data = response.json()
    print("Response (JSON):")
    print(json.dumps(data, indent=2))  # Pretty print JSON if applicable
    with open("dynascenes.json", 'w') as writefile:
        writefile.write(json.dumps(data,indent=2))
except json.JSONDecodeError:
    print("Response (Text):")
    print(response.text) #Print raw text if response is not JSON

    print(f"Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")