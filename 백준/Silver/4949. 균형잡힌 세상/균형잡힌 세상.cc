#include <iostream>
#include <string>
#include <stack>
using namespace std;
int main(void) {

	while (true) {
		string str;
		getline(cin, str);
		if (str == ".") break;

		stack<char> s;
		bool is_valid = true;

        for (auto c : str) {
            if (c == '(' || c == '[') {
                s.push(c);
            }
            else if (c == ')') {
                if (s.empty() || s.top() != '(') {
                    is_valid = false;
                    break;
                }
                s.pop();
            }
            else if (c == ']') {
                if (s.empty() || s.top() != '[') {
                    is_valid = false;
                    break;
                }
                s.pop();
            }
        }

		if (!s.empty()) is_valid = false;

		if (is_valid) cout << "yes\n";
		else cout << "no\n";
	}
}