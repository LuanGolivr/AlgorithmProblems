#include <iostream>
#include "FriendClassesInter.h"

using namespace std;


void testando3( teste1 &t3, int val){
    t3.teste = val;
}

int main (){

    teste1 t1;
    teste2 t2;

    testando3(t1, 15);
    t2.testando2(t1, 20);
    cout << "size of do objeto t1 e t2 " << sizeof(t1) << " , " << sizeof(t2);

    return 0;
}