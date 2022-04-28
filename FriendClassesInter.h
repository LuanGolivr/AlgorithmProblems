#include <iostream>

using namespace std;

class teste1 {
    friend void testando3(teste1 &, int );
    friend class teste2;
public:
    void testando();
private:
    int teste;
};

class teste2 {
public:
    void testando2(teste1 & , int);

};


void teste1::testando() {
    int teste = 1;
}


void teste2::testando2(teste1 &t4, int valores){
    cout << "Vou alterar o valor da variavel teste da class teste1 atraves de uma funcao da class teste2" << endl;
    cout << "Valor anterior a alteracao: " << t4.teste << endl;
    t4.teste = valores;
    cout << "Valor posterior a alteração: "<< t4.teste << endl;
}