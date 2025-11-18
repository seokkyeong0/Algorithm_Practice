#include <iostream>
#include <string>
using namespace std;

int main() {
	string cp;
	cin >> cp;

	int R = 0;
	int C = 0;
	for (int i = 1; i <= cp.size(); i++) {
		for (int j = 1; j <= cp.size(); j++) {
			if (i <= j && i * j == cp.size() && R < i) {
				R = i;
				C = j;
			}
		}
	}

	for (int i = 0; i < R; i++) {
		int a = 0;
		for (int j = 0; j < C; j++) {
			cout << cp[i + a];
			a += R;
		}
	}
}