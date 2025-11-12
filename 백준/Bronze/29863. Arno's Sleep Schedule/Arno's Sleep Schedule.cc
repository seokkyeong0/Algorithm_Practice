#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (a >= 20 && a <= 23) {
        cout << 24 - a + b;
    }
    else {
        cout << b - a;
    }
}