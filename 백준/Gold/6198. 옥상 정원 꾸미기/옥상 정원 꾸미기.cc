#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n;
stack<int> s;
long long result, h;

int main() {

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> h;
        while (!s.empty() && s.top() <= h) {
            s.pop();
        }
        result += s.size();
        s.push(h);
    }

    cout << result;
    return 0;
}