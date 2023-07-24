#include <stdio.h>
#include <stdint.h>

const int PIN_BUZZER = 25;

hw_timer_t* timer = NULL;
bool value = true;
int frequency = 20; // 20 to 20000
int tempo = 1;
int frequencia = 0;

void IRAM_ATTR onTimer() {
  value = !value;
  digitalWrite(PIN_BUZZER, value); 
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

typedef struct __attribute__((__packed__)){
    uint16_t tamanho_buffer, frequencia[4900], duracao[4900];
}Nota;

Nota musica; 

uint8_t buffer[20000];
uint16_t sizeBuffer = 0;// como são esperadas mensagens com dados de 16bits (2 bytes), cria-se esta variável para decodificar os 2 bytes e transformar em um número
uint16_t tamanhoMusica = 0;

void setup() {
    Serial.begin(115200);
    pinMode(PIN_BUZZER, OUTPUT);    // sets the digital pin as output
    setupTimer();
}

void loop() {
    
   if (Serial.available() > 0){ //se houver comunicação serial 
    
      Serial.readBytes(buffer, 2); //recebe 2 bytes e coloca-os nas primeiras posições da variável buffer (no caso buffer[0], buffer[1])

      memcpy(&sizeBuffer, buffer, 2); //os 2 bytes recebidos indicam o número de bytes que o micro receberá para completar a mensagem
      Serial.readBytes(buffer+2, sizeBuffer ); //recebe os dados e coloca nas próximas posições da variável buffer
      
      tamanhoMusica = (int) (sizeBuffer/2);

      memcpy(musica.frequencia, buffer + 2, tamanhoMusica); //faz os bytes recebidos irem para a variável estruturada criada
      memcpy(musica.duracao, buffer + 2 + tamanhoMusica, tamanhoMusica );
      //ele copia sizeBuffer/2 (metade da mensagem) pois os dados foram enviados enfileirados, primeiro os dados de frequeência depois os dados de tempos de execução de cada frequência
      
      //toca a música
      for(int i = 0; i < tamanhoMusica ; i++)
        tone(musica.frequencia[i], musica.duracao[i]);

      //desliga a música
      timerAlarmDisable(timer);

   }
}
