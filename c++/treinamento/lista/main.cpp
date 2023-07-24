#include <iostream>
#include <cstdlib>
#include <time.h>
#include <list>

using std::cin;
using std::cout;
using std::list;

void cadastrarLista(list<int> *lista, bool isFrente){
    
    if(isFrente)
        lista->push_front(rand());
    else
        lista->push_back(rand());

}

void infoGeralLista(list<int> *lista){
    
    cout << "\n******\t Info Geral sobre a lista ******\n";

    if(lista->size() > 0){

        cout << "\n Tamanho: " << lista->size();
        cout << "\n Tamanho maximo: " << lista->max_size();
        cout << "\n Frente do Lista: " << lista->front() << "\n";
        cout << "\n Fim da Lista: " << lista->back() << "\n";

    }else{
        cout << "\n Lista vazia !\n " ;
    }
    
    cout << "\n******************************************\n";

}

void retirarDaLista(list<int> *lista, bool isEsvaziar, bool isFrente){
    
    if(lista->empty()) return;

    if(isEsvaziar){ //se for só pra esvaziar então não importa a ordem
        do{
            lista->pop_front();
        }while(!lista->empty());

        return;
    }

    if(isFrente)
        lista->pop_front();
    else
        lista->pop_back();

}

void trocarComListaAuxiliar(list<int> *lista, list<int> *listaAuxiliar){
    lista->swap(*listaAuxiliar);
}

void ordenarLista(list<int> *lista){
    lista->sort();
}

void reverterLista(list<int> *lista){
    lista->reverse();
}



int main(){

    srand(time(0));

    list<int> lista;
    list<int> listaAuxliar;

    int opcaoMenu = 99; 
    while(opcaoMenu != 0){
        cout << "1 - Cadastrar na frente\n";
        cout << "2 - Cadastrar na atrás\n";
        cout << "3 - Info Geral da Lista\n";
        cout << "4 - Retirar 1 da Frente\n";
        cout << "5 - Retirar 1 da Trás\n";
        cout << "6 - Esvaziar\n";
        cout << "7 - Trocar com lista auxiliar\n";
        cout << "8 - Ordenar\n";
        cout << "9 - Inverter Lista\n";
        cout << "0 - Sair\n";
        cout << "Digite uma opcao do menu: \t";
        cin >> opcaoMenu;

        switch (opcaoMenu)
        {
        case 1:
            cadastrarLista(&lista, true);
            break;
        case 2:
            cadastrarLista(&lista, false);
            break;
        case 3:
            infoGeralLista(&lista);
            break;
        case 4:
            retirarDaLista(&lista, false, true);
            break;
        case 5:
            retirarDaLista(&lista, false, false);
            break;
        case 6:
            retirarDaLista(&lista, true, false);
            break;
        case 7:
            trocarComListaAuxiliar(&lista, &listaAuxliar);
            break;
        case 8:
            ordenarLista(&lista);
            break;
        case 9:
            reverterLista(&lista);
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