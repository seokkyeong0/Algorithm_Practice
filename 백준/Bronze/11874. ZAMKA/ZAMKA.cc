#include <iostream>
using namespace std;

int main(void) {
	int L, D, X;

	cin >> L;
	cin >> D;
	cin >> X;

	bool cut = true;
	int L_sum = 0, D_sum = 0;
	for (int a = 0; a <= 1; a++) {
		for (int b = 0; b < 10; b++) {
			for (int c = 0; c < 10; c++) {
				for (int d = 0; d < 10; d++) {
					for (int e = 0; e < 10; e++) {
						if ((a + b + c + d + e) == X && (a * 10000 + b * 1000 + c * 100 + d * 10 + e * 1) >= L && cut) {
							L_sum = a * 10000 +
									b * 1000 +
									c * 100 +
									d * 10 +
									e * 1;
							cut = false;
						}
						if ((a + b + c + d + e) == X && (a * 10000 + b * 1000 + c * 100 + d * 10 + e * 1) <= D) {
							D_sum = a * 10000 +
									b * 1000 +
									c * 100 +
									d * 10 +
									e * 1;
						}
					}
				}
			}
		}
	}

	cout << L_sum << '\n' << D_sum;
}