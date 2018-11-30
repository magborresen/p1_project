void GenderPick() { //funktionen som brugeren bruger til at vælge.
  delay(2000);
  lcd.clear();
  lcd.println("Hvad er dit koen?   ");

  while (digitalRead(Knap) == LOW) {

    SensorVal = analogRead(A0);
    if (ValValue < SensorVal) { //drejes knappen mod venstre
      lcd.setCursor(6, 1);
      lcd.print("Kvinde");
      Answers[0] = 1;
    }

    else if (SensorVal < ValValue) { //drejes knappen mod højre
      lcd.setCursor(6, 1);
      lcd.print(" Mand ");
      Answers[0] = 2;
    }
  }
}

void Alder () { // Funktion til valg af alder.
  lcd.clear();
  lcd.print("Indtast alder");
  delay(1000);
  while (digitalRead(Knap) == LOW) { //Stuck så længe knap=lav.
    Serial.println(analogRead(A0));

    if (analogRead(A0) > 100 and analogRead(A0) <999 ) {
      Serial.println(analogRead(A0)); // Hvis read af A0 er mellem
      lcd.setCursor(5, 1);            // 100 og 1000, kør dette.
      int Alder = analogRead(A0);
      lcd.println(Alder);
      lcd.setCursor(7, 1);
      lcd.print("    ");
      delay(50);
    }

      else if (analogRead(A0) > 10 and analogRead(A0) <99 ) {
      Serial.println(analogRead(A0)); // Hvis read af A0 er mellem
      lcd.setCursor(5, 1);            // 10 og 100, kør dette.
      int Alder = analogRead(A0);
      lcd.println(Alder);
      lcd.setCursor(6, 1);
      lcd.print("    ");
      delay(50);
     }
  }
  Answers[1] = analogRead(A0)/10;  // Gem og præsenter svar i serial monitor.
  Serial.print("Answers are ");
  Serial.print(Answers[0]);
  Serial.print(" and ");
  Serial.print(Answers[1]);
  lcd.clear();
  delay(5000);
}
