#include <iostream>

using namespace std;
int main() {
    int b[2] = { 0, 0 };
    int d[2] = { 0, 0 };
    int j[2] = { 0, 0 };

    cin >> b[0] >> b[1];
    cin >> d[0] >> d[1];
    cin >> j[0] >> j[1];

    int b_dist = max(abs(j[0] - b[0]), abs(j[1] - b[1]));
    int d_dist = abs(j[0] - d[0]) + abs(j[1] - d[1]);

    if (b_dist > d_dist) cout << "daisy";
    else if (b_dist < d_dist) cout << "bessie";
    else cout << "tie";
}