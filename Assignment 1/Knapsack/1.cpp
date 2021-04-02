#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream f ("a.in");
ofstream g ("a.out");
const int nr_maxim_elemente = 100;
const int k_maxim = 100;


int v[nr_maxim_elemente+5];
int dp[nr_maxim_elemente+5][k_maxim+5];

/*
dp[i][j] = suma maxima care poate fi formata din primele i elemente, astfel incat suma <= j
dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]]+v[i]), daca v[i]<=j
           dp[i-1][j], daca v[i]>j
           0, daca i==0 sau j==0
*/

int main()
{
    int n, k;
    f>>n;
    f>>k;
    for(int i=0; i<n; i++)
    {
        f>>v[i];
    }

    for(int i=0; i<=n; i++)
    {
        for(int j=0; j<=k; j++)
        {
            if(i==0 || j==0)
            {
                dp[i][j]=0;
            }
            else
            {
                if(v[i]<=j)
                {
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-v[i]] + v[i]);
                }
                else
                {
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
    }

    cout<<dp[n][k];
    return 0;
}