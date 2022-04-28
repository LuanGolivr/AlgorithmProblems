#include <iostream>

using namespace std;

void alterar(int *vetor){
    
    for(int i = 0; i < 3; i++){
        vetor[i] = i * 10;
    }

}

int main (){

    int *arr = new int[3];

    alterar(arr);

    delete [] arr;
    
    return 0;
}