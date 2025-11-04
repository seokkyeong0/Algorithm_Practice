#include <iostream>

using namespace std;
int main() {
	char A;
	cin >> A;
	if (A == 'M') cout << "MatKor";
	else if (A == 'W') cout << "WiCys";
	else if (A == 'C') cout << "CyKor";
	else if (A == 'A') cout << "AlKor";
	else if (A == '$') cout << "$clear";
}