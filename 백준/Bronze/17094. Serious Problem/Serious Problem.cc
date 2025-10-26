#include <iostream>
#include <string>
using namespace std;

int main() {
    int s;
    string str;
    cin >> s;
    cin >> str;

    int cnt_2 = 0;
    int cnt_e = 0;

    for (auto c : str) {
        if (c == '2') cnt_2++;
        else cnt_e++;
    }

    if (cnt_2 > cnt_e) cout << 2;
    else if (cnt_2 < cnt_e) cout << 'e';
    else cout << "yee";
}