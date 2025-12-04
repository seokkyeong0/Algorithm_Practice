#include <iostream>

using namespace std;

int main() {
	int A, P, C;
	cin >> A >> P >> C;
	
	if (A + C < P) cout << P;
	else cout << A + C;
}