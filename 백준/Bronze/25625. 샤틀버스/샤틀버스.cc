#include <iostream>
using namespace std;
int main(void) {
	int x, y;
	cin >> x >> y;
	if (x > y) {
		cout << x + y;
	}
	else {
		cout << y % x;
	}
}