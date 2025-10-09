#include <iostream>
#include <stack>

int v[100000];

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int floor = 0, result = 0;

    stack<char> st;
    for (auto c : s) {
        if (st.empty()) {
            st.push(c);
            floor++;
        }
        else if (!st.empty() && st.top() == '(' && c == '(') {
            st.push(c);
            floor++;
        }
        else if (!st.empty() && st.top() == ')' && c == '(') {
            st.push(c);
            floor++;
        }
        else if (!st.empty() && st.top() == '(' && c == ')') {
            st.push(c);
            floor--;
            v[floor] += 1;
        }
        else if (!st.empty() && st.top() == ')' && c == ')') {
            st.push(c);
            if (floor > 0) {
                result += (v[floor] + 1);
                v[floor - 1] += v[floor];
                v[floor] = 0;
                floor--;
            }
        }
    }
    cout << result;
}