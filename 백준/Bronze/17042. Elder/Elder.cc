#include <iostream>
using namespace std;

int N;
char cur;
bool visited[128];
int cnt;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> cur >> N;
	visited[cur] = 1;
	while (N--) {
		char x, y; cin >> x >> y;
		if (y == cur) visited[x] = 1, cur = x;
	}

	for (char c = 'A'; c <= 'Z'; c++) {
		if (visited[c]) cnt++;
	}

	cout << cur << '\n' << cnt;
}