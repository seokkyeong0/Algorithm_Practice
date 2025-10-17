#include <iostream>
#include <string>

using namespace std;
int main(void) {
	int n;
	cin >> n;

	while (n--) {
		string s;
		cin >> s;

		cout << s[0];
		for (int i = 1; i < s.size(); i++) {
			if (s[i] != s[i - 1]) cout << s[i];
		}
		cout << '\n';
	}
}