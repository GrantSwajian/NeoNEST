int vals[6]; // variable to store the value read
int del = 500;
int i = 0;

void setup() {
  Serial.begin(9600);           //  setup serial
  
}

void loop() {
  for(i = 0; i < 6; i ++){
    vals[i] = analogRead(i);
    Serial.println(vals[i]);
  }
  Serial.println("\n");
  delay(del);
}
