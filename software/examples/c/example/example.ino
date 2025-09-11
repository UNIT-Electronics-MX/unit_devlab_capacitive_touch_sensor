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
