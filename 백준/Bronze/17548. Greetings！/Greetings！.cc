#include <iostream>
using namespace std;

int main() {
	string hey;
	cin >> hey;
	for (auto c : hey) {
		if (c == 'e') {
			for (int i = 0; i < 2; i++)
				cout << c;
		}
		else {
			cout << c;
		}
	}
}