#include <iostream>
#include <list>
#include <string>
using namespace std;

int main(void) {
	int N, K;

	list<int> L = {};
	list<int> result = {};
	auto p = L.begin();

	cin >> N >> K;
	for (int i = 1; i < N + 1; i++) L.insert(p, i);
	p = L.begin();

	while (L.size() != 0) {
		for (int i = 0; i < K; i++) {
			if (p != L.end()) {
				p++;
			}
			else {
				p = L.begin();
				p++;
			}
		}
		result.push_back(*(--p));
		p = L.erase(p);
	}

	cout << '<';
	auto r = result.begin();
	for (int i = 0; i < result.size() - 1; i++) {
		cout << *r << ',' << ' ';
		r++;
	}
	cout << *r;
	cout << '>';
}