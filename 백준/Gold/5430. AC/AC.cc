#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string p;
        cin >> p;

        int n;
        cin >> n;

        string x;
        cin >> x;

        deque<int> dq;
        int num = 0;
        bool in_num = false;

        for (char c : x) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
                in_num = true;
            }
            else if (c == ',' || c == ']') {
                if (in_num) {
                    dq.push_back(num);
                    num = 0;
                    in_num = false;
                }
            }
        }

        bool reversed = false;
        bool error = false;

        for (char c : p) {
            if (c == 'R') {
                reversed = !reversed;
            }
            else if (c == 'D') {
                if (dq.empty()) {
                    error = true;
                    break;
                }
                if (!reversed) dq.pop_front();
                else dq.pop_back();
            }
        }

        if (error) {
            cout << "error\n";
            continue;
        }

        cout << '[';
        if (!dq.empty()) {
            if (!reversed) {
                for (int i = 0; i < dq.size(); i++) {
                    cout << dq[i];
                    if (i != dq.size() - 1) cout << ',';
                }
            }
            else {
                for (int i = dq.size() - 1; i >= 0; i--) {
                    cout << dq[i];
                    if (i != 0) cout << ',';
                }
            }
        }
        cout << "]\n";
    }
}