#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    int num;
    for (int i = 0; i < n; i++) {
        int zack = 0;
        int mack = 0;
        vector<int> v;

        for (int j = 0; j < 10; j++) {
            cin >> num;
            v.push_back(num);
        }
        
        for (auto i : v) {
            if (i == 17) zack++;
            else if (i == 18) mack++;
        }

        for (auto i : v) cout << i << ' ';
        cout << "\n";
        if (zack > 0 && mack == 0) cout << "zack\n\n";
        else if (mack > 0 && zack == 0) cout << "mack\n\n";
        else if (zack > 0 && mack > 0) cout << "both\n\n";
        else cout << "none\n\n";
    }
}