# Examples

## MicroPython Example

### Basic Touch Detection

```python
from machine import Pin
import time

# Usamos GPIO6
touch_pin = Pin(12, Pin.IN, Pin.PULL_DOWN)

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
```

### Usage
1. Upload this file to your MicroPython board
2. Connect the touch sensor to the specified pin
3. Run the script to see touch detection in action

## C/Arduino Examples

### example.ino (C++)

```ino
// Arduino C++ version of the given MicroPython code

const int touchPin = 12; // GPIO12
volatile unsigned int pulseCount = 0;

void IRAM_ATTR onPulse() {
    pulseCount++;
    Serial.print("¡Pulso detectado! Total: ");
    Serial.println(pulseCount);
}

void setup() {
    Serial.begin(115200);
    pinMode(touchPin, INPUT_PULLDOWN); // Use INPUT_PULLDOWN if available, else use INPUT
    attachInterrupt(digitalPinToInterrupt(touchPin), onPulse, RISING); // Rising edge interrupt
    Serial.println("Esperando pulsos del sensor capacitivo en GPIO12...");
}

void loop() {
    delay(1000); // Main loop does nothing, everything handled by interrupt
}
```

