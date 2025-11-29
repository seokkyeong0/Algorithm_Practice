#include <iostream>

using namespace std;

int main() {
	int t, n;
	cin >> t;

	for (int a = 1; a <= t; a++) {
		cin >> n;
		cout << "Case " << a << ":\n";
		for (int i = 1; i < 7; i++) {
			for (int j = 1; j < 7; j++) {
				if(i + j == n && i <= j)
					cout << '(' << i << ',' << j << ")\n";
			}
		}
	}
}