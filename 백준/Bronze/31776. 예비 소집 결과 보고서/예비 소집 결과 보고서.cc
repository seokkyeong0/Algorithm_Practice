#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;

	int cnt = 0;
	while (N--) {
		int a, b, c;
		bool good_team = false;

		cin >> a >> b >> c;
		
		if (a <= b && a <= c && b <= c && a != -1 && b != -1 && c != -1) {
			good_team = true;
		}
		else if (a >= 0 && b == -1 && c == -1) {
			good_team = true;
		}
		else if (a >= 0 && b >= 0 && c == -1 && a <= b) {
			good_team = true;
		}
		
		if (good_team) {
			cnt++;
		}
	}

	cout << cnt;
}