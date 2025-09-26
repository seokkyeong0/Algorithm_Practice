#include <iostream>
#include <vector>

using namespace std;
int main() {
	vector<int> v(9);
	vector<int> z(7);

	for (int i = 0; i < 9; i++) {
		cin >> v[i];
	}

	for (int a = 0; a < 9; a++) {
		for (int b = a + 1; b < 9; b++) {
			for (int c = b + 1; c < 9; c++) {
				for (int d = c + 1; d < 9; d++) {
					for (int e = d + 1; e < 9; e++) {
						for (int f = e + 1; f < 9; f++) {
							for (int g = f + 1; g < 9; g++) {
								if (v[a] + v[b] + v[c] + v[d] + v[e] + v[f] + v[g] == 100) {
									z[0] = v[a];
									z[1] = v[b];
									z[2] = v[c];
									z[3] = v[d];
									z[4] = v[e];
									z[5] = v[f];
									z[6] = v[g];
								}
							}
						}
					}
				}
			}
		}
	}

	int temp;
	for (int i = 0; i < 7; i++) {
		for (int j = i; j < 7; j++) {
			if (z[i] > z[j]) {
				temp = z[i];
				z[i] = z[j];
				z[j] = temp;
			}
		}
	}

	for (int i = 0; i < 7; i++) {
		cout << z[i];
		cout << "\n";
	}
}