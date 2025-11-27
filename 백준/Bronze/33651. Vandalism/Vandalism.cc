#include <iostream>
#include <string>
using namespace std;

int main() {
	string a;
	cin >> a;

	bool is_U = true;
	bool is_A = true;
	bool is_P = true;
	bool is_C = true;

	for (auto c : a) {
		if (c == 'U') is_U = false;
		else if (c == 'A') is_A = false;
		else if (c == 'P') is_P = false;
		else if (c == 'C') is_C = false;
	}

	if (is_U) cout << "U";
	if (is_A) cout << "A";
	if (is_P) cout << "P";
	if (is_C) cout << "C";
}