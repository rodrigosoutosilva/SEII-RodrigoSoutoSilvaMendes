#include <iostream>
using namespace std;

class car
{
public:
	string Name;
	string Color;
	double Price;

	car(string name, string color, double price)
	{
		Name = name;
		Color = color;
		Price = price;
	}

	void getinfo()
	{
		cout << "Nome: " << Name << endl;
		cout << "Cor: " << Color << endl;
		cout << "Preco : " << Price << endl;
	}

};

int main()
{

	car mycar("UNO", "prata", 1000);

	mycar.getinfo();

	system("pause>0");
}
