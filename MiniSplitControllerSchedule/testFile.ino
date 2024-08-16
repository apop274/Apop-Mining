#include <Wire.h>
#include <RTClib.h>
#include <Servo.h>

RTC_DS3231 rtc;
Servo myservo;

const int onHour = 8;   // 8 AM
const int offHour = 18; // 6 PM

void setup() {
  myservo.attach(9);  // Attach the servo to pin 9
  

  // Initialize the RTC
 // if (!rtc.begin()) {
  //  Serial.println("Couldn't find RTC");
 //   while (1);
 // }

  if (rtc.lostPower()) {
    //Serial.println("RTC lost power, setting time!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__))); // Set the time to the current compile time
  }

  // Initialize the servo to the resting position
  myservo.write(0);
  delay(1000);  // Give it a second to move to the initial position
}

void loop() {
  DateTime now = rtc.now();

  int currentHour = now.hour();
  int currentMinute = now.minute();

  // Trigger the servo at 8 AM
  if (currentHour == onHour && currentMinute == 0) {
    myservo.write(45);
    //Serial.println("Servo ON (8 AM)");
    delay(2000);  // Hold position for 2 seconds to ensure the button is fully pressed
    myservo.write(0);
    //Serial.println("Servo OFF");
    delay(60000);  // Wait for a minute to prevent repeated triggering within the same minute
  }

  // Trigger the servo at 6 PM
  else if (currentHour == offHour && currentMinute == 0) {
    myservo.write(45);
    //Serial.println("Servo ON (6 PM)");
    delay(2000);  // Hold position for 2 seconds to ensure the button is fully pressed
    myservo.write(0);
   // Serial.println("Servo OFF");
    delay(60000);  // Wait for a minute to prevent repeated triggering within the same minute
  }

  delay(1000);  // Check every second
}
