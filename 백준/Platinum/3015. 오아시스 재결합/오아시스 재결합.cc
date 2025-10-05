#include <iostream>
#include <stack>
using namespace std;

int main() {
	int n, x, cnt;
	cin >> n;

	stack<pair<int, int>> s;
	long long ans = 0;

	for (int i = 0; i < n; i++) {
		cin >> x;
		cnt = 1;
		while (!s.empty() && s.top().first <= x) {
			ans += s.top().second;
			if (s.top().first == x) cnt += s.top().second;
			s.pop();
		}

		if (!s.empty()) ans++;
		s.push({ x, cnt });
	}
	cout << ans;
}