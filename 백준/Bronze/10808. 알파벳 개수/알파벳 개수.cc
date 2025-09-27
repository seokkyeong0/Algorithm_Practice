#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	vector<int> alpha(26);
	string s;
	cin >> s;

	// 초기화
	for (int i = 0; i < alpha.size(); i++) {
		alpha[i] = 0;
	}

	// 연산
	for (int i = 0; i < s.size(); i++) {
		alpha[int(s[i]) - 97] += 1;
	}

	// 출력
	for (int i = 0; i < alpha.size(); i++) {
		cout << alpha[i] << ' ';
	}
}