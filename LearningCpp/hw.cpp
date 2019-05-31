#include <iostream>
#include <math.h>
using namespace std;

int main() {
    cout << "Enter your 1st coordinate: ";
    int x1, y1;
    cin >> x1 >> y1;
    cout << "Enter your 2nd coordinate: ";
    int x2, y2;
    cin >> x2 >> y2;
    cout << endl << "Distance: " << sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) << endl;
}