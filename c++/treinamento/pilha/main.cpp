#include <iostream>
#include <stack>
#include <cstdlib>
#include <time.h>

using std::cout;
using std::cin;
using std::stack;

void cadastrarPilha(stack<int> *pilha){

    pilha->push(rand());
    
}

void infoGeralPilha(stack<int> *pilha){

        cout << "\n******\t Info Geral sobre a pilha ******\n";

    if(pilha->size() > 0){

        cout << "\nTamanho: " << pilha->size();
        cout << "\nTopo do Pilha: " << pilha->top() << "\n";

    }else{
        cout << "\n Lista vazia !\n " ;
    }
    
    cout << "\n******************************************\n";
}

void retirarDaPilha(stack<int> *pilha, bool isEsvaziar){

    if(pilha->empty()) return;
    
    if(!isEsvaziar) pilha->pop();
    else {
        do{
            pilha->pop();
        }while(!pilha->empty());
    }

}

void usarPilhaAuxiliar(stack<int> *pilha, stack<int> *pilhaAuxiliar){
    pilha->swap(*pilhaAuxiliar);
}

int main(){

    srand(time(0));

    stack<int> pilha;
    stack<int> pilhaAuxliar;

    int opcaoMenu = 99; 
    while(opcaoMenu != 0){
        cout << "1 - Cadastrar\n";
        cout << "2 - Info Geral da Pilha\n";
        cout << "3 - Retirar 1 da Pilha\n";
        cout << "4 - Esvaziar Pilha\n";
        cout << "5 - Trocar com Pilha Auxliar\n";
        cout << "0 - Sair do Menu\n";
        cout << "Digite uma opcao do menu: \t";
        cin >> opcaoMenu;

        switch (opcaoMenu)
        {
        case 1:
            cadastrarPilha(&pilha);
            break;
        case 2:
            infoGeralPilha(&pilha);
            break;
        case 3:
            retirarDaPilha(&pilha, false);
            break;
        case 4:
            retirarDaPilha(&pilha, true);
            break;
        case 5:
            usarPilhaAuxiliar(&pilha, &pilhaAuxliar);
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