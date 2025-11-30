#include <iostream>
#include <string>

using namespace std;

int main() {
	int N;
	cin >> N;

	string ptr, del;
	cin >> ptr >> del;

	while (N--) {
		for (int i = 0; i < ptr.size(); i++) {
			if (ptr[i] == '1') ptr[i] = '0';
			else ptr[i] = '1';
		}
	}

	if (ptr == del) cout << "Deletion succeeded";
	else cout << "Deletion failed";
}