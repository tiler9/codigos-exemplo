
void taskBlink(void *pvParameters);
void taskBlink2(void *pvParameters);

#define LED_PIN 2


void setup() {
  
  xTaskCreatePinnedToCore(taskBlink, "taskBlink",  1024,  NULL,  1,  NULL,  1); // INICIALIZAÇÃO DAS TASKS
  xTaskCreatePinnedToCore(taskBlink2, "taskBlink2",  1024,  NULL,  1,  NULL,  1); // INICIALIZAÇÃO DAS TASKS
  
  Serial.begin(9600);
  Serial.println("setup()");

  pinMode(LED_PIN, OUTPUT);
}

void loop() {

}

/* SOLUÇÃO: RODAR TUDO EM PARALELO, UTILIZANDO TASKS, PARA ISSO FOI IMPLEMENTADO O FREERTOS */

void taskBlink(void *pvParameters){
  char bt1_cmd;
  for(;;){

    digitalWrite(LED_PIN, HIGH);
    vTaskDelay(500); 

  } 
}

void taskBlink2(void *pvParameters){
  char bt1_cmd;
  for(;;){

    digitalWrite(LED_PIN, LOW);
    vTaskDelay(500); 

  } 
}
