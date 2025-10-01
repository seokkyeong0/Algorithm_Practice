#include <iostream>
#include <cmath>

using namespace std;
int main(void) {
	int N, K;
	cin >> N >> K;

	int S, Y;
	int room[6][2] = { {0, 0} , {0, 0} , {0, 0} , {0, 0} , {0, 0} , {0, 0} };

	for (int i = 0; i < N; i++) {
		cin >> S >> Y;
		room[Y-1][S] += 1;
	}

	int total = 0;
	for (int i = 0; i < 6; i++) {
		total += ceil(float(room[i][0]) / K) + ceil(float(room[i][1]) / K);
	}

	cout << total;
}