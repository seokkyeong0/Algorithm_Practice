#include <iostream>
using namespace std;

int main() {
    int fence[100] = {0};

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    for (int i = a; i < b; i++) {
        fence[i] = 1;
    }

    for (int i = c; i < d; i++) {
        fence[i] = 1;
    }

    int ans = 0;
    for (auto i : fence) ans += i;
    cout << ans;
}