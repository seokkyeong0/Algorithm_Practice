#include <iostream>

using namespace std;
int main(void) {
	int k, d, a;
	char t1, t2;

	cin >> k >> t1 >> d >> t2 >> a;
	if (k + a < d || d == 0) {
		cout << "hasu";
	}
	else {
		cout << "gosu";
	}
}