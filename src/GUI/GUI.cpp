#include <LiquidCrystal.h>
#include <Nytest.cpp>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


void GUIsetup() {
  lcd.begin(16, 2);
  pinMode(8, INPUT_PULLUP);
  digitalWrite(8, LOW);
 lcd.print("Hoeretester");
}

void GUIloop() {

while (digitalRead(8) == LOW) {

}
lcd.clear();
delay(2000);

}
