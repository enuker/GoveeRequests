import requests
import json

url = "https://openapi.api.govee.com/router/api/v1/user/devices"
api_key = "6dc03b20-0ea0-4fde-a9c1-b245e3342864"

headers = {
    "Content-Type": "application/json",
    "Govee-API-Key": api_key,
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    
    # Attempt to parse JSON, if the response is JSON
    try:
        data = response.json()
        print("Response (JSON):")
        print(json.dumps(data, indent=2))  # Pretty print JSON if applicable
        with open("Device_params.json", 'w') as outfile:
            outfile.write(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("Response (Text):")
        print(response.text) #Print raw text if response is not JSON

    print(f"Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
    