#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream f ("a.in");
ofstream g ("a.out");

int main()
{
    // x - variabila de tip ifstream
    int x;
    // Cele 3 variabile de tip int sunt:
    // k - dat in problema
    // elem_max - care va retine elementul maxim din sirul dat
    // sum - suma calculata prin algoritmul tip greedy
    int k, elem_max=0, sum=0;
    f>>k;
    while(f>>x)
    {
        if(x<=k)
        {
            sum+=x; 
            k-=x;  
        }
        elem_max=max(elem_max, x);
    }

    cout<<max(elem_max, sum);
    return 0;
}