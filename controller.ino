#include <Servo.h>
Servo piv;
int newData;
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  piv.attach (9);
  Serial.setTimeout(10);
}
void loop() {
//oof
}
void serialEvent(){
  newData = Serial.read();
    if(newData == '1'){
      piv.write(180);
      digitalWrite(2,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(3,LOW);
    }else if(newData ==  '2'){
      piv.write(0);
      digitalWrite(4,HIGH);
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
    }else if(newData == '3'){
      piv.write(90);
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
    }else{
      piv.write(90);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
    }
}
