#include <iostream>
#include <string>

using namespace std;
int main(void) {
	int N, M;
	cin >> N >> M;

	string s1[10], s2[10];
	for (int i = 0; i < N; i++) {
		cin >> s1[i];
	}

	for (int i = 0; i < N; i++) {
		cin >> s2[i];
	}

	string s3[10];
	bool is_eyfa = true;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M * 2; j++) {
			s3[i] += s1[i][j/2];
		}
		
		if (s3[i] != s2[i]) {
			is_eyfa = false;
            break;
		}
	}

	if (is_eyfa) cout << "Eyfa";
	else cout << "Not Eyfa";
}