#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main()
{
    int p;
    cin >> p;
    while (p--)
    {
        int i, n, a, b;
        cin >> n >> a >> b;

        if (abs(a - b) % 2 == 1)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
    }

    return 0;
}