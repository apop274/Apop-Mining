//7.22.24

//     this is the official piece of code that will turn it on at 8 am and off at 6 pm
#include <EEPROM.h>
#include <Servo.h>

Servo myservo;
const unsigned long oneDayMillis = 86400000;  // 24 hours in milliseconds
const unsigned long onTimeMillis = 28800000;  // 8 AM in milliseconds from midnight
const unsigned long offTimeMillis = 64800000; // 6 PM in milliseconds from midnight

unsigned long previousMillis = 0;
unsigned long currentMillis = 0;
unsigned long startMillis;

void setup() {
  myservo.attach(9);  // Attach the servo to pin 9
  Serial.begin(9600);

  // Read saved start millis from EEPROM
  EEPROM.get(0, startMillis);

  // If the saved startMillis is invalid (first run), initialize it
  if (startMillis == 0 || startMillis >= oneDayMillis) {
    startMillis = millis();
    EEPROM.put(0, startMillis);
  }
}

void loop() {
  currentMillis = millis();
  unsigned long elapsedMillis = (currentMillis + startMillis) % oneDayMillis;

  // Calculate current hour based on elapsedMillis
  if (elapsedMillis >= onTimeMillis && elapsedMillis < onTimeMillis + 2000) {
    // Move servo to 45 degrees to simulate pressing the button
    myservo.write(45);
    Serial.println("Servo ON");
    delay(2000);  // Hold position for 2 seconds to ensure the button is fully pressed

    // Move servo back to 0 degrees
    myservo.write(0);
    Serial.println("Servo OFF");
  } else if (elapsedMillis >= offTimeMillis && elapsedMillis < offTimeMillis + 2000) {
    // Move servo to 45 degrees to simulate pressing the button
    myservo.write(45);
    Serial.println("Servo ON");
    delay(2000);  // Hold position for 2 seconds to ensure the button is fully pressed

    // Move servo back to 0 degrees
    myservo.write(0);
    Serial.println("Servo OFF");
  }

  // Save start millis to EEPROM every hour
  if ((elapsedMillis % 3600000) < 1000) {
    EEPROM.put(0, startMillis);
  }

  delay(1000);  // Check every second
}





/*

//               this is the code for testing (every 10 seconds)
#include <EEPROM.h>
#include <Servo.h>

Servo myservo;
const unsigned long interval = 10000;  // 10 seconds in milliseconds

unsigned long previousMillis = 0;
unsigned long currentMillis = 0;

void setup() {
  myservo.attach(9);  // Attach the servo to pin 9
  Serial.begin(9600);

  // Read saved millis from EEPROM
  EEPROM.get(0, previousMillis);
}

void loop() {
  currentMillis = millis();

  // Check if 10 seconds have passed
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Move servo to 45 degrees
    myservo.write(30);
    //Serial.println("Servo ON");
    delay(2000);  // Pause for 2 seconds to ensure the button is fully pressed

    // Move servo back to 0 degrees
    myservo.write(0);
    //Serial.println("Servo OFF");
  }

  // Save current millis to EEPROM every interval
  if ((currentMillis - previousMillis) < 1000) {
    EEPROM.put(0, currentMillis);
  }
}
*/