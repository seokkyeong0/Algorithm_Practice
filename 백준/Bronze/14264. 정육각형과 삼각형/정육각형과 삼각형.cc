#include <iostream>
#include <cmath>
using namespace std;

int main() {
	double length;
	cin >> length;

	cout << fixed;
	cout.precision(10);
	cout << (length * sqrt(3)) * length / 4.0;
}