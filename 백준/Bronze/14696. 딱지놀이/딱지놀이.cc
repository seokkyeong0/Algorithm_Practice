#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int t1[5] = { 0 };
        int t2[5] = { 0 };

        int a;
        cin >> a;
        for (int j = 0; j < a; j++) {
            int n;
            cin >> n;
            t1[n]++;
        }

        int b;
        cin >> b;
        for (int j = 0; j < b; j++) {
            int k;
            cin >> k;
            t2[k]++;
        }

        if (t1[4] != t2[4]) cout << (t1[4] > t2[4] ? 'A' : 'B');
        else if (t1[3] != t2[3]) cout << (t1[3] > t2[3] ? 'A' : 'B');
        else if (t1[2] != t2[2]) cout << (t1[2] > t2[2] ? 'A' : 'B');
        else if (t1[1] != t2[1]) cout << (t1[1] > t2[1] ? 'A' : 'B');
        else cout << 'D';
        cout << '\n';
    }
}