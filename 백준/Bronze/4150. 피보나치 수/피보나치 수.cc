#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector <string> fibonacci;

int main() {
	int n;
	cin >> n;

	fibonacci.push_back("0");
	fibonacci.push_back("1");
	
	for (int i = 2; i <= n; i++) {
		int a = fibonacci[i - 1].size(), b = fibonacci[i - 2].size(), res = 0, add = 0;
		string result, temp;
		for (int j = a - 1; j >= 0; j--) {
			if (j - (a - b) >= 0) res = (fibonacci[i - 1][j] - 48) + (fibonacci[i - 2][j - (a - b)] - 48) + add;
			else res = fibonacci[i - 1][j] - 48 + add;
			if (res >= 10) {
				res -= 10;
				add = 1;
			}
			else add = 0;
			temp = result;
			result = to_string(res) + temp;
			if (j == 0 && add == 1) {
				temp = result;
				result = to_string(add) + temp;
			}
		}
		fibonacci.push_back(result);
	}

	cout << fibonacci[n];

	return 0;
}