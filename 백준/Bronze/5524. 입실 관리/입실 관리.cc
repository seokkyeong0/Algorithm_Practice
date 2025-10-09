#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] >= 'A' && s[j] <= 'Z')
                s[j] += 32;
        }
        cout << s << '\n';
    }
}