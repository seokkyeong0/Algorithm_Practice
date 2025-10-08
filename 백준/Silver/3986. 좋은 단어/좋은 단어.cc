#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        stack<char> S;

        string A;
        cin >> A;
        for (auto c : A) {
            if (S.empty()) {
                S.push(c);
            }
            else if (!S.empty() && c == 'A') {
                if (S.top() == 'A') S.pop();
                else S.push(c);
            }
            else if (!S.empty() && c == 'B') {
                if (S.top() == 'B') S.pop();
                else S.push(c);
            }
        }

        if (S.empty()) cnt++;
    }

    cout << cnt;
}