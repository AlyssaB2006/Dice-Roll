#include "Arduino.h"

#include "Servo.h"

int servoPin = 9;
Servo twist;

void setup() {
  Serial.begin(9600);
  twist.attach(servoPin);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 't') {
      twist.write(0);
      delay(1000);
      twist.write(180);
      delay(3200);
    }
  }
}

