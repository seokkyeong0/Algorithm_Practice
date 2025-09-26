#include <iostream>

using namespace std;
int main() {
	long long A, B, temp;
	cin >> A >> B;

	if (A > B) {
		temp = A;
		A = B;
		B = temp;
	}

	if (B - A < 2) {
		cout << 0;
	}
	else {
		cout << B - A - 1 << '\n';
		for (long long i = A + 1; i < B; i++) {
			cout << i << ' ';
		}
	}
}