#include <iostream>
#include <string>

using namespace std;
int main() {
	string s;
	getline(cin, s);

	for (auto c : s) {
		if (int(c) >= 'A' && int(c) <= 'Z') {
			if (int(c) + 13 > 'Z') {
				cout << char((int(c) + 13) - 26);
			}
			else {
				cout << char(int(c) + 13);
			}
		}
		else if (int(c) >= 'a' && int(c) <= 'z'){
			if (int(c) + 13 > 'z') {
				cout << char((int(c) + 13) - 26);
			}
			else {
				cout << char(int(c) + 13);
			}
		}
		else {
			cout << c;
		}
	}
}