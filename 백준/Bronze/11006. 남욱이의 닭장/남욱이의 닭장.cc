#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	while (T--) {
		int N, M;
		cin >> N >> M;
		cout << (M * 2) - N << ' ' << M - ((M * 2) - N) << '\n';
	}
}