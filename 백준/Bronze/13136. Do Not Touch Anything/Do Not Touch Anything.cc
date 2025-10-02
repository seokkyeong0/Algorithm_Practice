#include <iostream>
#include <cmath>

using namespace std;
int main(void) {
	long double R, C, N;

	cin >> R >> C >> N;

	long long x = ceil(R / N);
	long long y = ceil(C / N);

	cout << x * y;
}