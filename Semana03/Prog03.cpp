#include <iostream>
using namespace std;

int main()
{
    int luckyn[3] = { 1,2,3 };
    cout << luckyn[2] << endl;


    int* luckyp = luckyn;

    cout << luckyp << " " << *luckyp << endl;
    luckyp++;
    cout << luckyp << " " << *luckyp << endl;



    system("pause>0");
}
