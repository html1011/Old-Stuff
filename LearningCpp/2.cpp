#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout << (((n % 2 == 1) || (n % 2 == 0 && n >= 6 && n <= 20)) ? "Weird" : "Not Weird") << endl; 
    return 0;
}
