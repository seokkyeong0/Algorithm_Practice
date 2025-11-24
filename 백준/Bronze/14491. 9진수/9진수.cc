#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;

	vector <int> v;

	while (T >= 1) {
		v.push_back(T % 9);
		T /= 9;
	}

	for (int i = v.size() - 1; i >= 0; i--) {
		cout << v[i];
	}
}