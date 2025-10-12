#include <iostream>
#include <string>
using namespace std;

int main() {
    string taebo;
    cin >> taebo;

    int cnt = 0;
    for (auto c : taebo) {
        if (c == '@') {
            cnt++;
        }
        else if (c == '(') {
            cout << cnt << ' ';
            cnt = 0;
        }
     }
    cout << cnt;
}