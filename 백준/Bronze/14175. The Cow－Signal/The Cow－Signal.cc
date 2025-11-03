#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main() {
	int M, N, K;
	cin >> M >> N >> K;

	string s;
	vector <string>v;
	for (int i = 0; i < M; i++) {
		cin >> s;
		v.push_back(s);
	}

	for (int i = 0; i < v.size(); i++) {
		for (int k = 0; k < K; k++) {
			for (auto c : v[i]) {
				for (int j = 0; j < K; j++)
					cout << c;
			}
			cout << '\n';
		}
	}
}