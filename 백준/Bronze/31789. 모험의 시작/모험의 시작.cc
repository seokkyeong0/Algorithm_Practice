#include <iostream>
using namespace std;

int main(void) {
	int N, X, S;
	cin >> N;
	cin >> X >> S;

	int C, P;
	bool we_can = false;
	for (int i = 0; i < N; i++) {
		cin >> C >> P;
		if (C <= X && S < P) we_can = true;
	}

	if (we_can) cout << "YES";
	else cout << "NO";
}