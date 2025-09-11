#include <Arduino.h>

const int TOUCH_PIN = 6;              
volatile unsigned long pulseCount = 0; 


void IRAM_ATTR onPulse() {
  pulseCount++;
  Serial.print("¡Pulso detectado! Total: ");
  Serial.println(pulseCount);
}

void setup() {
  Serial.begin(115200);
  
  pinMode(TOUCH_PIN, INPUT_PULLDOWN);
  attachInterrupt(digitalPinToInterrupt(TOUCH_PIN), onPulse, RISING);

  Serial.println("Esperando pulsos del sensor capacitivo en GPIO6...");
}

void loop() {
  delay(1000);
}
