#include <iostream>
#include <cmath>
using namespace std;

int main() {
	long long x1, y1, r1;
	long long x2, y2, r2;

	cin >> x1 >> y1 >> r1;
	cin >> x2 >> y2 >> r2;

	long long dist = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

	if (dist < r1 + r2) cout << "YES";
	else cout << "NO";
}