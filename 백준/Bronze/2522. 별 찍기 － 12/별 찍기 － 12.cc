#include <iostream>
using namespace std;

int main(void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int a = 0; a < N - (i + 1); a++)
			cout << ' ';
		for (int b = 0; b < i + 1; b++)
			cout << '*';
		cout << '\n';
	}
	for (int i = 0; i < N - 1; i++) {
		for (int a = 0; a < i + 1; a++)
			cout << ' ';
		for (int b = 0; b < N - (i + 1); b++) {
			cout << '*';
		}
		cout << '\n';
	}
}