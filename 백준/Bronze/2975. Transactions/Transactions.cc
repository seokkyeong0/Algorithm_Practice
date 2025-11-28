#include <iostream>

using namespace std;

int main() {
	int money, wdp;
	char mode;

	while (true) {
		cin >> money >> mode >> wdp;

		if (mode == 'W') {
			if (money == 0 && wdp == 0) break;

			if (money - wdp >= - 200) cout << money - wdp << '\n';
			else cout << "Not allowed\n";
		}
		else if (mode == 'D') {
			cout << money + wdp << '\n';
		}
	}
}