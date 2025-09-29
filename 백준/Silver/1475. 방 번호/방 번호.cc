#include <iostream>
#include <string>
using namespace std;

int main() {
	string N;
	cin >> N;

	int cnt[10] = { 0 };
	for (auto c : N) cnt[int(c) - 48] += 1;

	float comb = (cnt[6] + cnt[9]) / 2.0;
	if (comb - int(comb) > 0) comb = int(comb) + 1;
	cnt[6] = comb;
	cnt[9] = comb;

	int max = cnt[0];
	for (int i = 0; i < 10; i++) {
		if (max < cnt[i]) max = cnt[i];
	}
	cout << max;
}