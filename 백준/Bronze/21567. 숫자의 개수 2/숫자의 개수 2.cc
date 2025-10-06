#include <iostream>
#include <string>

using namespace std;
int main(void) {
	long long n, mul = 1;
	int result[10] = {0};

	for (int i = 0; i < 3; i++) {
		cin >> n;
		mul *= n;
	}

	string mstr = to_string(mul);

	for (int i = 0; i < mstr.size(); i++) result[mstr[i] - 48] += 1;
	for (auto i : result) cout << i << '\n';
}