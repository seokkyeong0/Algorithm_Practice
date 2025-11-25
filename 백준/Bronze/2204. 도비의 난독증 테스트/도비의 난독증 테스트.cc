#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	while (true) {
		int n;
		cin >> n;
		if (n == 0) break;

		vector <pair<string, int>> v;
		vector <string> str;
		string tmp;
		for (int i = 0; i < n; i++) {
			cin >> tmp;
			str.push_back(tmp);
			for (int j = 0; j < tmp.size(); j++) {
				if (tmp[j] >= 97) tmp[j] -= 32;
			}
			v.push_back({tmp, i});
		}

		sort(v.begin(), v.end());
		cout << str[v.front().second] << '\n';
	}
}