#include <iostream>
#include <string>

using namespace std;
int main(void) {
	int N;
	string a, b;

	cin >> N;

	int cnt[26];
	bool is_possible;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;

		is_possible = true;
		for (int i = 0; i < 26; i++) cnt[i] = 0;
		for (auto c : a) cnt[c - 97] += 1;
		for (auto c : b) cnt[c - 97] -= 1;

		for (int i = 0; i < 26; i++) {
			if (cnt[i] != 0) is_possible = false;
		}

		if (is_possible) cout << "Possible\n";
		else cout << "Impossible\n";
	}
}