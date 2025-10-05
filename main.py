# poll_api.py

import requests

# Your API URL
url = "https://deb-auth-api.onrender.com/users"



try:
    response = requests.get(url, timeout=600)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
