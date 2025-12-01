#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for(int i = 0; i < T; i++) {
		int N;
		cin >> N;

		int num = 0;		
		for (int a = 0; a < 10; a++) {
			for (int b = 0; b < 10; b++) {
				for (int c = 1; c < 10; c++) {
					if (a <= b && b <= c && a * 100 + b * 10 + c <= N)
						num = a * 100 + b * 10 + c;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << num << '\n';
	}
}