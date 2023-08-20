#define LED_pin 13
#define buzzer_pin 11

int times = 10;

void setup(){
  Serial.begin(9600);
  pinMode(LED_pin, OUTPUT);
  pinMode(buzzer_pin, OUTPUT);
}

void loop(){
  if (Serial.available() > 0){
    String msg = Serial.readString();

    if(msg == "ON"){
      digitalWrite(LED_pin, HIGH);
    }

    else if(msg == "blink"){
      while (times != 0){
        digitalWrite(LED_pin, HIGH);
        delay(100);
        digitalWrite(LED_pin, LOW);
        delay(100);
        times -= 1;
      }
      times == 10;
    }

    else if (msg == "OFF"){
      digitalWrite(LED_pin, LOW);
    }

    else if (msg == "buzzer on"){
      digitalWrite(buzzer_pin, HIGH);
    }

    else if (msg == "buzzer off"){
      digitalWrite(buzzer_pin, LOW);
    }
   
    else{
      digitalWrite(LED_pin, HIGH);
      delay(100);
      digitalWrite(LED_pin, LOW);
    }
  }
}