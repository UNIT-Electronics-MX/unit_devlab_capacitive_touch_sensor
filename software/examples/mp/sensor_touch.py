from machine import Pin
import time

# Using GPIO12
touch_pin = Pin(12, Pin.IN, Pin.PULL_DOWN)

pulse_count = 0

def on_pulse(pin):
    global pulse_count
    pulse_count += 1
    print("Pulse detected! Total:", pulse_count)

# Interrupt on rising edge (adjust if your sensor is active-low)
touch_pin.irq(trigger=Pin.IRQ_RISING, handler=on_pulse)

print("Waiting for pulses from capacitive sensor on GPIO12...")

# Main loop
while True:
    time.sleep(1)  # Avoid using CPU, everything handled by interrupt
