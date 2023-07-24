#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct
{
    uint8_t data[3];
    uint8_t hora[3];
    uint8_t metodo;
    uint8_t dados[1];
} Log;

void main()
{

    printf("%d", sizeof(Log));
}