#include <iostream>
using namespace std;
int main() {
    int num {10};
    cout << "Enter an integer: ";
    cin >> num;
    cout << "Double " << num << " is " << num * 2 << endl;
    cout << "Triple " << num << " is " << num * 3 << endl;
}