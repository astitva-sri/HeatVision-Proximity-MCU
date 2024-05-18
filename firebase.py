import urequests as requests
import json

FIREBASE_URL = 'https://heatvison-proximity-default-rtdb.firebaseio.com/time.json'
FIREBASE_API_KEY = 'AIzaSyAWAEQLS3QKNoZrbY7hrT4a6ZNG9Whm2KU'

def get_auth_token(email, password):
    auth_data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    auth_response = requests.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}", json=auth_data)
    auth_response_data = auth_response.json()
    print("Auth Response:", auth_response_data)  # Debugging line
    if 'idToken' in auth_response_data:
        return auth_response_data['idToken']
    else:
        print("Authentication failed:", auth_response_data)
        return None

def push_timestamp(timestamp, token):
    data = {"timestamp": timestamp}
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = requests.post(FIREBASE_URL, data=json.dumps(data), headers=headers)
    print("Push Response:", response.status_code, response.text)  # Debugging line
    if response.status_code == 200:
        print("Timestamp pushed to Firebase")
    else:
        print("Failed to push timestamp to Firebase:", response.status_code, response.text)

