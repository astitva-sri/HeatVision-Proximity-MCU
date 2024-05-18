import time
import wifi
import firebase
import mlx90614
import led

# Wi-Fi credentials
SSID = 'realme 9 Pro+'
WIFI_PASSWORD = 'Code Red'

# Firebase credentials
EMAIL = 'detectivekonan87@gmail.com'
FIREBASE_PASSWORD = 'qwertyuiop'

# Main function to run the code
def main():
    # Connect to Wi-Fi
    wifi.connect(SSID, WIFI_PASSWORD)

    # Authenticate with Firebase
    auth_token = firebase.get_auth_token(EMAIL, FIREBASE_PASSWORD)
    if auth_token is None:
        print("Failed to authenticate with Firebase")
        return

    # Define temperature range
    MIN_TEMP = 35
    MAX_TEMP = 37

    # Main loop to continuously monitor temperature and push timestamp if temperature is within range
    last_push_time = 0
    while True:
        try:
            object_temp = mlx90614.read_temp(mlx90614.MLX90614_TOBJ1)
            print("Object Temperature:", object_temp)
            
            if MIN_TEMP <= object_temp <= MAX_TEMP:
                current_time = time.time()
                if current_time - last_push_time >= 30:
                    try:
                        firebase.push_timestamp(current_time, auth_token)
                        led.blink_led(2)  # Blink LED connected to GPIO pin 2
                        last_push_time = current_time
                    except Exception as e:
                        print("Error pushing timestamp to Firebase:", e)
        except Exception as e:
            print("Error reading temperature:", e)
        
        time.sleep(1)  # Adjust the delay according to your requirement

# Run the main function
main()

