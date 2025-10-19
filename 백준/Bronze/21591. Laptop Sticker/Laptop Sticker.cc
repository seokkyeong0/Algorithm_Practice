#include <iostream>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int wc, hc, ws, hs;
    cin >> wc >> hc >> ws >> hs;

    if (wc - 2 >= ws && hc - 2 >= hs) cout << 1;
    else cout << 0;
}