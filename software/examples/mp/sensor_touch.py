from machine import Pin
import time

# Usamos GPIO6
touch_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)

pulse_count = 0

def on_pulse(pin):
    global pulse_count
    pulse_count += 1
    print("¡Pulso detectado! Total:", pulse_count)

# Interrupción por flanco de subida (ajusta si tu sensor es activo-bajo)
touch_pin.irq(trigger=Pin.IRQ_RISING, handler=on_pulse)

print("Esperando pulsos del sensor capacitivo en GPIO6...")

# Bucle principal
while True:
    time.sleep(1)  # Evita usar CPU, todo se maneja por interrupción
