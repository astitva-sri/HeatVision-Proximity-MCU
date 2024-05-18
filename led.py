import machine
import time

def blink_led(pin):
    led_pin = machine.Pin(pin, machine.Pin.OUT)
    led_pin.value(1)  # Turn LED on
    time.sleep(5)     # Blink for 5 seconds
    led_pin.value(0)  # Turn LED off

