#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    long long a, b, c;
    cin >> a >> b >> c;

    long long result1 = (a * b) / c;
    long long result2 = (long long)(((double)a / b) * c);

    cout << max(result1, result2);
}