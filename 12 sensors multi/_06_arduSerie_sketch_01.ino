int vals[6];
const byte common = A0;  // where the multiplexer in/out port is connected

// the multiplexer address select lines (A/B/C)
const byte addressA = 6; // low-order bit
const byte addressB = 5;
const byte addressC = 4; // high-order bit

void setup ()
{
  Serial.begin (9600);
  pinMode (addressA, OUTPUT);
  pinMode (addressB, OUTPUT);
  pinMode (addressC, OUTPUT);
}  // end of setup

int readSensor (const byte which)
{
  // select correct MUX channel
  digitalWrite (addressA, (which & 1) ? HIGH : LOW);  // low-order bit
  digitalWrite (addressB, (which & 2) ? HIGH : LOW);
  digitalWrite (addressC, (which & 4) ? HIGH : LOW);  // high-order bit
  // now read the sensor
  return analogRead (common);
}  // end of readSensor

void loop ()
{
  // show sensor readings
  for (byte i = 0; i < 12; i++)
  {
    if (i < 8){
      vals[i] = readSensor(i);
    }
    else{
      rs = i-7
      vals[rs] = analogRead(i);
    }
     Serial.println(vals[i]);
  }
   Serial.println("\n");
  delay (1000);
} 
