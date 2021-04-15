#include <Wire.h>
#include <Adafruit_ADS1X15.h>
 
Adafruit_ADS1015 ads;
int vals[4]; // variable to store the value read
int del = 500;
int i = 0;
 
void setup(void)
{
ads.setGain(GAIN_TWO);
Serial.begin(9600);
Serial.println("Hello!");
 
Serial.println("Getting single-ended readings from AIN0..3");
Serial.println("ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)");
 
ads.begin();
}
 
void loop(void)
{
int16_t adc0, adc1, adc2, adc3;
 
adc0 = ads.readADC_SingleEnded(0);
adc1 = ads.readADC_SingleEnded(1);
adc2 = ads.readADC_SingleEnded(2);
adc3 = ads.readADC_SingleEnded(3);

 
for(i = 0; i < 8; i ++){
    if (i < 4){
    vals[i] = analogRead(i);
    }
    else{
      int t = i-4;
    vals[i] = (ads.readADC_SingleEnded(t));
    }
    Serial.println(vals[i]);
  }
  Serial.println("\n");
  delay(del);
}
