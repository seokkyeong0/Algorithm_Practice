#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M;
    cin >> N >> M;
    
    vector<long long> vn;
    vector<long long> vm;
    for (int i = 0; i < N; i++) {
        long long nn;
        cin >> nn;
        vn.push_back(nn);
    }

    for (int i = 0; i < M; i++) {
        long long aa;
        cin >> aa;
        vm.push_back(aa);
    }

    long long result = 0;
    for (auto i : vn) result += i;
    for (auto i : vm) result += i;
    cout << result;
}