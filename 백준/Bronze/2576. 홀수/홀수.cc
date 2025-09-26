#include <iostream>
#include <vector>

using namespace std;
int main() {
	int total = 0;
	int flag = 0;
	int odd_min = 0;
	vector<int> num(7);

	for (int i = 0; i < 7; i++) {
		cin >> num[i];
	}

	for (int i = 0; i < 7; i++) {
		if ((num[i] % 2) != 0) {
			total += num[i];
			if (!flag) {
				odd_min = num[i];
				flag = 1;
			}
			else {
				if (odd_min > num[i]) {
					odd_min = num[i];
				}
			}
		}
	}

	if (total == 0) {
		cout << -1;
	}
	else {
		cout << total << "\n";
		cout << odd_min;
	}
}