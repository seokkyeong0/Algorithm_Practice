#include <iostream>
using namespace std;

int main() {
    int t, n;
    char p1, p2;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n;
        int a = 0, b = 0;
        for (int j = 0; j < n; j++) {
            cin >> p1 >> p2;
            if (p1 == 'R' && p2 == 'P') {
                b++;
            }
            else if (p1 == 'R' && p2 == 'S') {
                a++;
            }
            else if (p1 == 'P' && p2 == 'R') {
                a++;
            }
            else if (p1 == 'P' && p2 == 'S') {
                b++;
            }
            else if (p1 == 'S' && p2 == 'R') {
                b++;
            }
            else if (p1 == 'S' && p2 == 'P') {
                a++;
            }
        }

        if (a > b) cout << "Player 1\n";
        else if (a < b) cout << "Player 2\n";
        else cout << "TIE\n";
    }
}