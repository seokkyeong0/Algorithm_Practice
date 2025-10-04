#include <iostream>
using namespace std;

int main() {
    int N;
    double A1, P1, R1, P2;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A1 >> P1 >> R1 >> P2;
        if ((A1 / 360.0) / P1 > 1.0 / P2) cout << "Slice of pizza\n";
        else cout << "Whole pizza\n";
    }
}