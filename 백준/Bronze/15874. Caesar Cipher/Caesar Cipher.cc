#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int k, s, low;
	string cipher;

	cin >> k >> s;
	cin.ignore();
	getline(cin, cipher);

	for (int i = 0; i < s; i++) {
		if (cipher[i] >= 65 && cipher[i] <= 90) {
			cipher[i] += (k % 26);
			if (cipher[i] > 90) {
				cipher[i] -= 26;
			}
		}
		else if ((cipher[i] >= 97 && cipher[i] <= 122)) {
			low = int(cipher[i]) + (k % 26);
			if (low > 122) {
				low -= 26;
				cipher[i] = char(low);
			}
			else {
				cipher[i] += (k % 26);
			}
		}
	}

	for (int i = 0; i < s; i++) {
		cout << cipher[i];
	}
}