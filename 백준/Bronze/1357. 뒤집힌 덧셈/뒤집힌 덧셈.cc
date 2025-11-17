#include <iostream>
#include <string>
using namespace std;

int Rev(string num) {
	int rev = 0;
	int cnt = 1;

	for (auto c : num) {
		rev += int(c - 48) * cnt;
		cnt *= 10;
	}
	return rev;
}

int main() {
	string x, y;
	cin >> x >> y;
	cout << Rev(to_string(Rev(x) + Rev(y)));
}