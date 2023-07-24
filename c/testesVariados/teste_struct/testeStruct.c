#include <stdio.h>
#include <stdint.h>

typedef struct {
    int frequencia, duracao; 
} Acorde;

void main(){

    Acorde x = (Acorde){.frequencia = 100, .duracao = 101};

    printf("frequencia: %d", x.frequencia);
    printf("\nduracao: %d", x.duracao);
}