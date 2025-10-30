#include <iostream>
#include <string>

using namespace std;
int main() {
	string num;
	cin >> num;

	int result = 0;
	int prev;
	for (auto c : num) {
		if (c == '0') {
			result += (10 * prev) - prev;
		}
		else {
			result += c - 48;
		}
		prev = int(c) - 48;
	}
	cout << result;
}