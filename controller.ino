int newData;
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  Serial.setTimeout(10);
}
void loop() {
//oof
}
void serialEvent(){
  newData = Serial.read();
    if(newData == '1'){
      digitalWrite(2,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(3,LOW);
    }else if(newData ==  '2'){
      digitalWrite(4,HIGH);
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
    }else if(newData == '3'){
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
    }else{
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
    }
}

