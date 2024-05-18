from machine import SoftI2C, Pin
import time

# MLX90614 I2C address
MLX90614_I2C_ADDR = 0x5A

# Register addresses for temperatures
MLX90614_TA = 0x06  # Ambient temperature register
MLX90614_TOBJ1 = 0x07  # Object temperature register

# Initialize I2C on the specified SDA and SCL pins
i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=100000)

def read_temp(register):
    """
    Reads temperature from a specified register of the MLX90614.
    
    Args:
        register: The register address from which to read the temperature.
    
    Returns:
        The temperature in Celsius.
    """
    try:
        # Read data from the sensor's register
        data = i2c.readfrom_mem(MLX90614_I2C_ADDR, register, 3)
        # Combine the bytes and convert to temperature in Celsius
        temp = (data[1] << 8) | data[0]
        temp = (temp * 0.02) - 273.15  # Convert from Kelvin to Celsius
        return temp
    except Exception as e:
        print(f"Error reading temperature: {e}")
        raise

# Test the sensor reading
if __name__ == "__main__":
    try:
        print("* MLX90614 Temperature Readings *")
        while True:
            # Read sensor values for object and ambient temperatures
            object_temp = read_temp(MLX90614_TOBJ1)
            ambient_temp = read_temp(MLX90614_TA)
            
            # Print the temperature readings with the degree symbol
            print("Object Temperature: {:>5.2f}°C".format(object_temp))
            print("Ambient Temperature: {:>5.2f}°C".format(ambient_temp))
            print("-" * 30)  # Print a separator line for clarity
            
            # Wait for a second before the next reading
            time.sleep(1)
    except KeyboardInterrupt:
        # Gracefully handle script termination by the user
        print('\nScript stopped by user')
    finally:
        # Any cleanup can be done here
        print('Goodbye!')

