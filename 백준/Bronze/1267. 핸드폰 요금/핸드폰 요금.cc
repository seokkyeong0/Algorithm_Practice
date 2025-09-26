#include <iostream>

using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, T;
	cin >> N;

	int y = 0, m = 0;
	for (int i = 0; i < N; i++) {
		cin >> T;
		y += ((T / 30) + 1) * 10;
		m += ((T / 60) + 1) * 15;
	}

	if (y > m) {
		cout << "M " << m;
	}
	else if (y < m) {
		cout << "Y " << y;
	}
	else {
		cout << "Y " << "M " << y;
	}
}