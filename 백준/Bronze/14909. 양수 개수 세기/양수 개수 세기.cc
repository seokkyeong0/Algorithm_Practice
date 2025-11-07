#include <iostream>
using namespace std;

int main(){
	int cnt = 0;

	while (1){
		int n;
		cin >> n;
		if (cin.eof() == 1) break;
		if (n > 0) cnt++;
	}

	cout << cnt << '\n';
	return 0;
}