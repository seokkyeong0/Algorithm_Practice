#include <iostream>

using namespace std;
int main() {
	int m, k;
	cin >> m >> k;

	if (m % k > 0) cout << "No";
	else cout << "Yes";
}