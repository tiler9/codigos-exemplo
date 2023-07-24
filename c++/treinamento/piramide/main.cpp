/*
Faça o programa que apresenta a seguinte saída, perguntando ao usuário o número máximo (no exemplo, 9). Este número deve ser sempre ímpar.
1 2 3 4 5 6 7 8 9
   2 3 4 5 6 7 8
      3 4 5 6 7
         4 5 6
            5   

*/

#include <iostream>

using std::cout;
using std::cin;

int main(){

    int numeroDigitado = 0;

    cout << "Digite um numero impar:";

    cin >> numeroDigitado;

    if(numeroDigitado <= 0){
        cout << "Numero digitado deve ser maior que 0 e impar";
    }else if(numeroDigitado % 2 == 0){
        cout << "Numero digitado deve ser maior que 0 e impar";
    }else{
        for(int i = 0; i <= numeroDigitado; i++){
            
            for(int j = i + 1; j <= numeroDigitado - i ; j++)
                cout << j << "\t";

            if(i*2 > numeroDigitado) //aqui é para o loop parar quando a pirâmide chegar no pico
                break;

            cout << "\n";
            for(int k = 0; k <= i; k++)  //aqui é para fazer o efeito de pirâmide no lado esquerdo
                cout << "\t";
        }
    }

    return 0;

}