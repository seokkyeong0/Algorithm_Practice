#include <iostream>

using namespace std;
int main(void) {
	int N;
	int p[11][2] = { {12, 1600}, {11, 894}, {11, 1327}, {10, 1311}, {9, 1004}, {9, 1178}, {9, 1357},
					 {8, 837}, {7, 1055}, {6, 556}, {6, 773} };

	cin >> N;
	cout << p[N - 1][0] << ' ' << p[N - 1][1];
}