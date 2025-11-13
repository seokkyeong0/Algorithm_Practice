#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    cin >> a;

    bool is_valid = true;
    for (int i = 0; i < 3; i++) {
        if (a[i] != '5') {
            is_valid = false;
            break;
        }
    }

    if (is_valid) cout << "YES";
    else cout << "NO";
}