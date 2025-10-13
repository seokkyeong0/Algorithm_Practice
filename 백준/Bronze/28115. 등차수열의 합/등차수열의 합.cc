#include <iostream>
#include <vector>

using namespace std;
int main(void) {
	int N;
	cin >> N;

	vector<int> v(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i];
	}

	bool check = true;
	if (v.size() < 3) check = true;
	else {
		int sub = v[1] - v[0];
		for (int i = 0; i < N - 1; i++) {
			if (v[i + 1] - v[i] != sub) check = false;
		}
	}

	if (check) {
		if (v.size() == 1) {
			cout << "YES\n";
			cout << v[0]*2 << '\n' << -v[0];
		}
		else if (v.size() == 2) {
			cout << "YES\n";
			cout << v[0] * 2 << ' ' << v[1] * 2 << '\n';
			cout << -v[0] << ' ' << -v[1];
		}
		else {
			cout << "YES\n";
			for (auto i : v) cout << i * 2 << ' ';
			cout << '\n';
			for (auto i : v) cout << -i << ' ';
		}
	}
	else {
		cout << "NO";
	}
}