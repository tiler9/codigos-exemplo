#include <stdio.h>
#include <stdint.h>

/*
uint8_t *a1;
uint16_t *a2;

uint8_t *r1;
float *r2;
*/
uint16_t *n1, *n2, *n3;
uint16_t v1, v2, v3;

uint8_t buffer[40];

uint8_t x[5];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
}


void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    
    Serial.readBytes(buffer, 1);
    Serial.readBytes(buffer+1, buffer[0]);
    
  
  if(buffer[1] == 1){
    //faz nada por enquanto
    
    uint8_t aux;
    /*
    for(int i = 1; i <= buffer[0]; i++){
      buffer[i] = i;
    }
    */
    
    aux = buffer[2];
    buffer[2] = buffer[3];
    buffer[3] = aux;
    buffer[4] = 9;
    /**/
    
  }else if(buffer[1] == 2){

    //2 primeiras posições (0,1) são de 1 byte = 8
    //3 últimas (2,3,4) são de 2 bytes = 16
    //então eu tenho que mover o cursor de 2 em 2
    
    //para acessar a 3ª variável usando ponteiro de 16bits(buffer + 2)
    //para acessar a 4ª variável usando ponteiro de 16bits(buffer + 4)
    //para acessar a 5ª variável usando ponteiro de 16bits(buffer + 6)
  
    n1 = (uint16_t*) (buffer + 2);
    n2 = (uint16_t*) (buffer + 4);
    
    n3 = (uint16_t*) (buffer + 6);
    *n3 = *n1 + *n2;

    v1 = *n1;
    v2 = *n2;
    v3 = *n3;

  }else if(buffer[1] == 3){

    n1 = (uint16_t*) (buffer + 2);
    n2 = (uint16_t*) (buffer + 4);
    n3 = (uint16_t*) (buffer + 6);

    *n1 = v1;
    *n2 = v2;
    *n3 = v3;
    
  }

  Serial.write(buffer, buffer[0]+1);
  //Serial.write(buffer, 4);


/* //CASO ESTRANHO
     x[0] = (uint8_t) 5;
     x[1] = (uint8_t) 1;
     x[2] = (uint8_t) 1;
     x[3] = (uint8_t) 1;
     x[4] = (uint8_t) 1;
    
    Serial.write(x, 10);
*/
  }
}
