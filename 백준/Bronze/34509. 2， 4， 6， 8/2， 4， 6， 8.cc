#include <iostream>

using namespace std;
int main(void) {
	for (int i = 10; i < 100; i++) {
		if ((10 * (i % 10) + (i / 10)) % 4 == 0) {
			if (((i / 10) + (i % 10)) % 6 == 0) {
				if ((i / 10) != 8 && (i % 10) != 8) {
					cout << i;
					break;
				}
			}
		}
	}
}