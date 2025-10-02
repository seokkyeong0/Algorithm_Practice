#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void) {
	int N;
	cin >> N;

	deque<int> DQ;
	
	int n;
	string s;
	for (int i = 0; i < N; i++) {
		cin >> s;
		if (s == "push_front") {
			cin >> n;
			DQ.push_front(n);
		}
		else if (s == "push_back") {
			cin >> n;
			DQ.push_back(n);
		}
		else if (s == "pop_front") {
			if (DQ.size() != 0) {
				cout << DQ.front() << '\n';
				DQ.pop_front();
			}
			else cout << -1 << '\n';
		}
		else if (s == "pop_back") {
			if (DQ.size() != 0) {
				cout << DQ.back() << '\n';
				DQ.pop_back();
			}
			else cout << -1 << '\n';
		}
		else if (s == "size") {
			cout << DQ.size() << '\n';
		}
		else if (s == "empty") {
			if (DQ.size() != 0) cout << 0 << '\n';
			else cout << 1 << '\n';
		}
		else if (s == "front") {
			if (DQ.size() != 0) cout << DQ.front() << '\n';
			else cout << -1 << '\n';
		}
		else if (s == "back") {
			if (DQ.size() != 0) cout << DQ.back() << '\n';
			else cout << -1 << '\n';
		}
	}
}