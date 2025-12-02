#include <iostream>
#include <vector>

using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<long long> v;
    long long c;
    for (int i = 0; i < N; ++i) {
        cin >> c;
        v.push_back(c);
    }

    if (N == 1) {
        cout << v[0] - 1 << " " << v[0] << "\n";
        return 0;
    }

    long long P = 1;
    long long Q = v[N - 1];
    for (int i = N - 2; i >= 0; i--) {
        long long next_v = v[i];
        long long tmp = next_v * Q + P;
        P = Q;
        Q = tmp;

        long long g = gcd(P, Q);
        P /= g;
        Q /= g;
    }

    cout << Q - P << " " << Q;

    return 0;
}