#include <bits/stdc++.h>
using namespace std;

bool meet(int x1, int v1, int x2, int v2)
{
    if ((x1 > x2 && v1 >= v2) || (x1 < x2 && v1 <= v2) || (x1 == x2 && v1 != v2))
        return false;

    return (abs(x1 - x2) % abs(v1 - v2) == 0);
}

int main()
{
    int x1 = 8, v1 = 3, x2 = 5, v2 = 2;
    cout << meet(x1, v1, x2, v2);
}