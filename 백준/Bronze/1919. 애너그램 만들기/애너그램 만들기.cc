#include <iostream>
#include <string>
#include <cmath>

using namespace std;
int main(void) {
	string a, b;

	cin >> a >> b;

	int a_sum[26] = {};
	int b_sum[26] = {};

	for (int i = 0; i < a.size(); i++) a_sum[a[i] - 97] += 1;
	for (int i = 0; i < b.size(); i++) b_sum[b[i] - 97] += 1;

	int result = 0;
	for (int i = 0; i < 26; i++) result += (abs(a_sum[i] - b_sum[i]));
	cout << result;
}