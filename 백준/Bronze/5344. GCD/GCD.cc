#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	while (T--) {
		int a, b;
		cin >> a >> b;

		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}

		cout << a << '\n';
	}
}