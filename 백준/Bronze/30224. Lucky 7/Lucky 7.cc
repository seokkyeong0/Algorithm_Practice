#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    string num = to_string(N);

    bool is_seven = false;
    for (auto c : num) if (c == '7') is_seven = true;

    if (!is_seven && N % 7 > 0) {
        cout << 0;
    }
    else if (!is_seven && N % 7 == 0) {
        cout << 1;
    }
    else if (is_seven && N % 7 > 0) {
        cout << 2;
    }
    else if (is_seven && N % 7 == 0) {
        cout << 3;
    }
}