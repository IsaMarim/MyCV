#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

#define RightmotorF 7 //digitalpin 7 for right motor forward 
#define RightmotorB 8 //digital pin 8 for right motor Backward 
#define LeftmotorF 5 //digitalpin 5 for left motor forward 
#define LeftmotorB 6 //digital pin 6 for right motor Backward 
#define motorena 3 // Motor Controller
#define motorenb 11 // Motor Controller

void Backward() {
digitalWrite(LeftmotorF,LOW); 
digitalWrite(RightmotorF, LOW); 
digitalWrite(LeftmotorB,HIGH); 
digitalWrite(RightmotorB, HIGH);
}

void Forward() {
digitalWrite(RightmotorF, HIGH); 
digitalWrite(RightmotorB, LOW);
digitalWrite(LeftmotorF,HIGH); 
digitalWrite(LeftmotorB,LOW);
}

void Right() {
digitalWrite(RightmotorF, HIGH); 
digitalWrite(RightmotorB, LOW); 
digitalWrite(LeftmotorF,LOW); 
digitalWrite(LeftmotorB,LOW);
}

void Left() {
digitalWrite(RightmotorF, LOW); 
digitalWrite(RightmotorB, LOW); 
digitalWrite(LeftmotorF,HIGH); 
digitalWrite(LeftmotorB,LOW);
}

void movestop() {
digitalWrite(RightmotorF, LOW);
digitalWrite(RightmotorB, LOW); 
digitalWrite(LeftmotorF,LOW); 
digitalWrite(LeftmotorB,LOW);
}

void setup() {
Serial.begin(9600);
mySwitch.enableReceive(0); // Receiver on interrupt 0 => that is pin #2

// put your setup code here, to run once:
pinMode(RightmotorF, OUTPUT);//declaring these pins as output to control them pinMode(RightmotorB, OUTPUT);
pinMode(LeftmotorF,OUTPUT);
pinMode(LeftmotorB,OUTPUT);
pinMode(motorena,OUTPUT);
pinMode(motorenb,OUTPUT);
analogWrite(motorena, 80); 
analogWrite(motorenb, 80);
pinMode(LED_BUILTIN, OUTPUT); 
}

void loop() {

    if (mySwitch.available()) {
        int value = mySwitch.getReceivedValue();
        if (value == 0) { 
            Serial.print("Unknown encoding"); 
        } 
        
        else {

            if (mySwitch.getReceivedValue() == 274820){ 
                Forward();
                Serial.println("Forward");
            }
            else if (mySwitch.getReceivedValue() == 274824) { 
                Backward();
                Serial.println("Back");
            }
            else if (mySwitch.getReceivedValue() == 274818) { 
                Right();
                Serial.println("Right");
            }
            else if (mySwitch.getReceivedValue() == 449204) { 
                Left();
                Serial.println("Left");
            }
            else if (mySwitch.getReceivedValue() == 449202) {
                movestop();
            }
        
            else {

                Serial.print("Received ");
                Serial.print( mySwitch.getReceivedValue() );
                Serial.print(" / ");
                Serial.print( mySwitch.getReceivedBitlength() );
                Serial.print("bit ");
                Serial.print("Protocol: ");
                Serial.println( mySwitch.getReceivedProtocol() );
            }
        }
    
    mySwitch.resetAvailable();

    }
}