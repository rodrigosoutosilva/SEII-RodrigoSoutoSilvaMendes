#include <iostream>
using namespace std;


float soma(float a, float b);
void uhul(void);

int main()
{


	float r = soma(5, 6);

	cout <<"A soma eh: "<< r << endl;

	uhul();


}

float soma(float a, float b)
{
	return a + b;
}

void uhul(void)
{
	cout << "uhul" << endl;
}