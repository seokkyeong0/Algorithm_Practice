#include <iostream>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	if (N % M == 0) cout << N / M;
	else cout << (N / M) + 1;
}