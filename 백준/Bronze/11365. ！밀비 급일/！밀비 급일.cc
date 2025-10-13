#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        string s;
        getline(cin, s);
        if (s == "END") {
            break;
        }
        else {
            for (int i = s.size() - 1; i >= 0; i--) {
                cout << s[i];
            }
            cout << '\n';
        }
    }
}