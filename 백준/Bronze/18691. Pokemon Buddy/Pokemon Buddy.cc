#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        int G, C, E;
        cin >> G >> C >> E;

        if (G == 1) G = 1;
        else if (G == 2) G = 3;
        else G = 5;

        if (C >= E) cout << 0 << '\n';
        else cout << (E - C) * G << '\n';
    }
}