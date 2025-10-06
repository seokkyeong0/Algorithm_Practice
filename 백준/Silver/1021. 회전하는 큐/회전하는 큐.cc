#include <iostream>
#include <deque>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	int cnt = 0;
	int A;
	deque<int> dq_1, dq_2;
	for (int i = 0; i < N; i++) {
		dq_1.push_back(i + 1);
		dq_2.push_back(i + 1);
	}

	while (M--) {
		cin >> A;
		if (dq_1.front() == A && dq_2.front() == A) {
			dq_1.pop_front();
			dq_2.pop_front();
		}
		else {
			int d1 = 0, d2 = 0;
			while (dq_1.front() != A) {
				dq_1.push_back(dq_1.front());
				dq_1.pop_front();
				d1++;
			}

			while (dq_2.front() != A) {
				dq_2.push_front(dq_2.back());
				dq_2.pop_back();
				d2++;
			}

			cnt += min(d1, d2);

			if (dq_1.front() == A && dq_2.front() == A) {
				dq_1.pop_front();
				dq_2.pop_front();
			}
		}
	}

	cout << cnt;
}