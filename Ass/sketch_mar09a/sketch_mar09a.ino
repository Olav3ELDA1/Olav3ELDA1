#include <ESP8266WiFi.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(D5, OUTPUT);

  Serial.begin(115200);
  Serial.println();

  WiFi.begin("data_iot", "elev1234");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(D4, HIGH);
  delay(500);
  digitalWrite(D4, LOW);
  delay(500);
}
