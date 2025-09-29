#include <iostream>
#include <string>
using namespace std;

int main() {
	int A, B, C, tot;

	cin >> A;
	cin >> B;
	cin >> C;
	tot  = A;
	tot *= B;
	tot *= C;

	int N[10] = {0};
	string num = to_string(tot);
	for (int i = 0; i < num.size(); i++) N[num[i] - 48] += 1;
	for (auto i : N) cout << i << '\n';
}