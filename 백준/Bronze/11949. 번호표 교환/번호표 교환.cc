#include <iostream>
#include <vector>

using namespace std;
int main(void) {
	int N, M;
	cin >> N >> M;

	vector<int> v(N);
	for (int i = 0; i < N; i++) {
		int A;
		cin >> A;
		v[i] = A;
	}

	for (int i = 1; i <= M; i++) {
		for (int j = 0; j < N - 1; j++) {
			if (v[j] % i > v[j + 1] % i) {
				int temp = v[j + 1];
				v[j + 1] = v[j];
				v[j] = temp;
			}
		}
	}

	for (auto i : v) cout << i << '\n';
}