#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;

	int cnt = 0;
	bool is_start = false;
	bool is_end = false;

	while (!is_end) {
		if (!is_start) getline(cin, s);

		if (s == "고무오리 디버깅 시작") {
			is_start = true;
		}

		while (is_start) {
			getline(cin, s);
			if (s == "고무오리 디버깅 끝") {
				is_start = false;
				is_end = true;
			}

			if (s == "문제") cnt++;
			else if (s == "고무오리" && cnt == 0) cnt += 2;
			else if (s == "고무오리") cnt--;
		}
	}

	if (cnt == 0) cout << "고무오리야 사랑해";
	else cout << "힝구";
}
