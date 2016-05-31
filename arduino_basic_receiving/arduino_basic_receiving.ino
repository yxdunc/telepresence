#include <Servo.h>

const int POS_MIN=0;
const int POS_MAX=90;
const int broche1=9; //
const int broche2=10;//brocheservo

int position_servo=0; 

int OctetReception=0; 

Servo mon_servo;
Servo mon_servo1;

void setup(){
  Serial.begin(115200); //connexion série 115200 bauds

  mon_servo.attach(broche1/*, POS_MIN, POS_MAX*/);
  mon_servo1.attach(broche2/*, POS_MIN, POS_MAX*/);

  pinMode(broche1, OUTPUT);
  pinMode(broche2, OUTPUT);

  mon_servo.write(20);
  mon_servo1.write(22);

  delay(200);
}

void loop(){
  if (Serial.available()>0) { //if receiving octet
    OctetReception=Serial.read();
    Serial.println(OctetReception);

    if (OctetReception < 50)
    {
      position_servo=map(OctetReception,0,50,0,180);
      mon_servo.write(position_servo);
    }
    else if (OctetReception >= 50)
    {
     position_servo=map(OctetReception - 49,0,50,0,180);
      mon_servo1.write(position_servo);
    }
  }
} 
