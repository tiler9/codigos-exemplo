#include <iostream>
#include <queue>
#include <cstdlib>
#include <time.h>

using std::cout;
using std::cin;
using std::queue;

void cadastrarNaFila(queue<int> *fila){

    fila->push(rand());
    
}

void infoGeralFila(queue<int> *fila){

        cout << "\n******\t Info Geral sobre a fila ******\n";

    if(fila->size() > 0){

        cout << "\n Tamanho: " << fila->size();
        cout << "\n Frente do Fila: " << fila->front() << "\n";
        cout << "\n Fim da Fila: " << fila->back() << "\n";

    }else{
        cout << "\n Fila vazia !\n " ;
    }
    
    cout << "\n******************************************\n";
}

void retirarDaFila(queue<int> *fila, bool isEsvaziar){

    if(fila->empty()) return;
    
    if(!isEsvaziar) fila->pop();
    else {
        do{
            fila->pop();
        }while(!fila->empty());
    }

}

void usarFilaAuxiliar(queue<int> *fila, queue<int> *filaAuxiliar){
    fila->swap(*filaAuxiliar);
}

int main(){

    srand(time(0));

    queue<int> fila;
    queue<int> filaAuxliar;

    int opcaoMenu = 99; 
    while(opcaoMenu != 0){
        cout << "1 - Cadastrar\n";
        cout << "2 - Info Geral da Fila\n";
        cout << "3 - Retirar 1 da Fila\n";
        cout << "4 - Esvaziar Fila\n";
        cout << "5 - Trocar com Fila Auxliar\n";
        cout << "0 - Sair do Menu\n";
        cout << "Digite uma opcao do menu: \t";
        cin >> opcaoMenu;

        switch (opcaoMenu)
        {
        case 1:
            cadastrarNaFila(&fila);
            break;
        case 2:
            infoGeralFila(&fila);
            break;
        case 3:
            retirarDaFila(&fila, false);
            break;
        case 4:
            retirarDaFila(&fila, true);
            break;
        case 5:
            usarFilaAuxiliar(&fila, &filaAuxliar);
            break;
        case 0:
        
            return 0;
            break;
        
        default:
            cout << "Opcao Invalida\n";
            break;
        }
    }

    return 0;

}