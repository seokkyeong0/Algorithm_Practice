#include <iostream>
#include <stack>

using namespace std;
int main(void) {
	int n, h, w;

	while (true) {
		cin >> n;
		if (n == 0) break;

		stack<pair<int, int>> s;
		long long ans = 0;
		for (int i = 0; i < n; i++) {
			cin >> h;
			w = i;
			while (!s.empty() && s.top().first >= h) {
				ans = max(ans, 1LL * (i - s.top().second) * s.top().first);
				w = s.top().second;
				s.pop();
			}
			s.push({ h, w });
		}

		while (!s.empty()) {
			ans = max(ans, 1LL * (n - s.top().second) * s.top().first);
			s.pop();
		}
		cout << ans << '\n';
	}
}