#include <iostream>
#include <list>
#include <string>
using namespace std;

int main(void) {
	int T;
	string s;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> s;
		list<char> L = {};
		list<char>::iterator c;
		for (int a = 0; a < s.size(); a++) {
			if ((s[a] != '<') && (s[a] != '>') && (s[a] != '-')) {
				if (L.size() == 0) {
					L.push_front(s[a]);
					c = L.end();
				}
				else {
					L.insert(c, s[a]);
				}
			}
			else if (s[a] == '>' && (L.size() != 0)) {
				if (c != L.end())
					c++;
			}
			else if (s[a] == '-' && (L.size() != 0)) {
				if (c != L.begin())
					c = L.erase(--c);
			}
			else if (s[a] == '<' && (L.size() != 0)){
				if (c != L.begin())
					c--;
			}
		}
		for (auto c : L) cout << c;
		cout << '\n';
	}
}