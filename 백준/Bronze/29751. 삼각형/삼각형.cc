#include <iostream>
#include <string>
using namespace std;

int main() {
    int W, H;
    cin >> W >> H;

    cout << fixed;
    cout.precision(1);
    cout << (W * H) / 2.0;
}