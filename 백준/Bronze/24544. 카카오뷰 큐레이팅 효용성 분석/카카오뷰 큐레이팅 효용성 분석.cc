#include <iostream>
#include <vector>

using namespace std;
int main(void) {
	int N;
	cin >> N;

	vector <int> v1, v2;
	
	int A;
	int total = 0;
	for (int i = 0; i < N; i++) {
		cin >> A;
		v1.push_back(A);
		total += A;
	}

	for (int i = 0; i < N; i++) {
		cin >> A;
		v2.push_back(A);
	}

	int M = 0;
	for (int i = 0; i < N; i++) {
		if (v2[i] == 0) M += v1[i];
	}

	cout << total << '\n' << M;
}