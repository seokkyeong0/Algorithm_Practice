#include <iostream>
#include <string>
#include <stack>
using namespace std;

string s;
stack<char> st;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> s;

    int sum = 0;
    int num = 1;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            num *= 2;
            st.push(s[i]);
        }
        else if (s[i] == '[') {
            num *= 3;
            st.push(s[i]);
        }
        else if (s[i] == ')') {
            if (st.empty() || st.top() != '(') {
                cout << 0;
                return 0;
            }
            if (s[i - 1] == '(') sum += num;
            st.pop();
            num /= 2;
        }
        else {
            if (st.empty() || st.top() != '[') {
                cout << 0;
                return 0;
            }
            if (s[i - 1] == '[') sum += num;
            st.pop();
            num /= 3;
        }
    }
    if (st.empty()) cout << sum;
    else cout << 0;
}