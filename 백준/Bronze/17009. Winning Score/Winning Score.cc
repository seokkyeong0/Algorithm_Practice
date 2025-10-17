#include <iostream>

using namespace std;
int main(void) {
	int apples = 0, bananas = 0;

	int tmp, shot;

	shot = 3;
	for (int i = 0; i < 3; i++) {
		cin >> tmp;
		apples += tmp * shot;
		shot--;
	}

	shot = 3;
	for (int i = 0; i < 3; i++) {
		cin >> tmp;
		bananas += tmp * shot;
		shot--;
	}

	if (apples > bananas) cout << 'A';
	else if (apples < bananas) cout << 'B';
	else cout << 'T';
}