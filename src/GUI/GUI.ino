
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int SensorVal = analogRead(A0);
const int Knap = 8;
const int ValValue = 500;
int Answers []= {0,0};

void setup() {
  lcd.begin(16, 2);
  pinMode(Knap, INPUT_PULLUP);
  lcd.print("Hoeretester");
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  GenderPick();
  Alder();
}
