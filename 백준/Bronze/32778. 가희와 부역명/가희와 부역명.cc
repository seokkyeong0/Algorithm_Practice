#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    getline(cin, a);

    bool i = true;
    for (auto c : a) {
        if (c == '(') {
            i = false;
            cout << '\n';
        }
        else if (c == ')') continue;
        else cout << c;
    }

    if (i) cout << '\n' << '-';
}