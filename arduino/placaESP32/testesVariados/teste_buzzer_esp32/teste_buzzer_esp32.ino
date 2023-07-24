const int PIN = 25;

hw_timer_t* timer = NULL;
bool value = true;
int frequency = 20; // 20 to 20000
int Pinofalante = 25;
int tempo = 1;
int frequencia = 0;

void IRAM_ATTR onTimer() {
  value = !value;
  digitalWrite(PIN, value); 
}

void setup() {
    Serial.begin(115200);
    pinMode(PIN, OUTPUT);    // sets the digital pin as output
    setupTimer();
}

void setupTimer() {
    // Use 1st timer of 4  - 1 tick take 1/(80MHZ/80) = 1us so we set divider 80 and count up 
    timer = timerBegin(0, 80, true);//div 80
    timerAttachInterrupt(timer, &onTimer, true);
}

void setFrequency(long frequencyHz){
    timerAlarmDisable(timer);
    timerAlarmWrite(timer, 1000000l / frequencyHz, true);
    timerAlarmEnable(timer);
}

void tone(long frequencyHz, long durationMs){
    setFrequency(frequencyHz);
    delay(durationMs);
}

void loop() {
  /*
    Serial.print(frequency); // in hz
    Serial.println(" hz");
    tone(frequency,1000);
    frequency+=100;
    if (frequency>=200000){
      frequency = 20;
    }
    */
    tone( 6262, 250); 
    tone( 6294, 250); 
    tone( 6330, 250); 
    tone( 6349, 250); 
    tone( 6392, 250); 
    /*
    for (frequencia = 4150; frequencia < 5800; frequencia += 1) 
    {
      tone( frequencia, tempo); 
      delay(1);
    }
    for (frequencia = 5800; frequencia > 4150; frequencia -= 1) 
    {
      tone( frequencia, tempo); 
      delay(1);
    }
    */
}
