const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 391;
const int gS = 415;
const int a = 440;
const int aS = 455;
const int b = 466;
const int cH = 523;
const int cSH = 554;
const int dH = 587;
const int dSH = 622;
const int eH = 659;
const int fH = 698;
const int fSH = 740;
const int gH = 784;
const int gSH = 830;
const int aH = 880;

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
  firstSection();
  
  //Toca a segunda variação
  secondSection();
  
  //Variação 1:
  tone(f, 250); 
  tone(gS, 500); 
  tone(f, 350); 
  tone(a, 125);
  tone(cH, 500);
  tone(a, 375); 
  tone(cH, 125);
  tone(eH, 650);
  
  delay(500);
  
  secondSection();
  
  //Variação 2:
  tone(f, 250); 
  tone(gS, 500); 
  tone(f, 375); 
  tone(cH, 125);
  tone(a, 500); 
  tone(f, 375); 
  tone(cH, 125);
  tone(a, 650);
  
  delay(650);
}

void firstSection()
{
  tone(a, 500);
  tone(a, 500); 
  tone(a, 500);
  tone(f, 350);
  tone(cH, 150); 
  tone(a, 500);
  tone(f, 350);
  tone(cH, 150);
  tone(a, 650);
  
  delay(500);
  
  tone(eH, 500);
  tone(eH, 500);
  tone(eH, 500); 
  tone(fH, 350);
  tone(cH, 150);
  tone(gS, 500);
  tone(f, 350);
  tone(cH, 150);
  tone(a, 650);
  
  delay(500);
}

void secondSection()
{
  tone(aH, 500);
  tone(a, 300);
  tone(a, 150);
  tone(aH, 500);
  tone(gSH, 325);
  tone(gH, 175);
  tone(fSH, 125);
  tone(fH, 125); 
  tone(fSH, 250);
  
  delay(325);
  
  tone(aS, 250);
  tone(dSH, 500);
  tone(dH, 325); 
  tone(cSH, 175); 
  tone(cH, 125); 
  tone(b, 125); 
  tone(cH, 250); 
  
  delay(350);
}
