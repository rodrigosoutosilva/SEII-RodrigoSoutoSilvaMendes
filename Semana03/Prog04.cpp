#include <iostream>
using namespace std;

class car
{
public:
	string name;
	string color;
	double price;
};

int main()
{
	car mycar;
	mycar.name = "Carro";
	mycar.color = "Preto";
	mycar.price = 1000;

	cout << "Nome: " << mycar.name << endl;
	cout << "Cor: " << mycar.color << endl;
	cout << "Preço : " << mycar.price << endl;

	system("pause>0");
}

