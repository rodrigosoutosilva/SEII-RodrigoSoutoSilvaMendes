#include <iostream>
using namespace std;

class car
{
private:
	string Name;
	string Color;
	double Price;
	bool isbroken;

public:
	car(string name, string color, double price)
	{
		Name = name;
		Color = color;
		Price = price;
		isbroken = false;
	}
	void getinfo()
	{
		cout << "Nome: " << Name << endl;
		cout << "Cor: " << Color << endl;
		cout << "Preco : " << Price << endl;
		cout << "Quebrado: " << isbroken << endl;
	}

	void crashcar()
	{
		cout << "QUEBROU" << endl;
		isbroken = true;
	}

	void repaircar()
	{
		cout << "CONCERTOU" << endl;
		isbroken = false;
	}

	void move()
	{
		if (isbroken)
		{
			cout << "PARA" << endl;
		}
		else
		{
			cout << "ANDA" << endl;
		}

	}


};

int main()
{

	car funo("UNO", "prata", 1000);
	car vgol("GOL", "verde", 1200);

	funo.getinfo();
	vgol.getinfo();

	funo.move();
	funo.crashcar();
	funo.move();
	funo.repaircar();
	funo.move();

	system("pause>0");
}
