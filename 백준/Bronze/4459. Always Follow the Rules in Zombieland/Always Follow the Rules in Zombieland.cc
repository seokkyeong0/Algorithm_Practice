#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int q;
    cin >> q;
    cin.ignore();
    vector <string> rules;

    while (q--) {
        string s;
        getline(cin, s);
        rules.push_back(s);
    }

    cin >> q;
    while (q--) {
        int num;
        cin >> num;

        if (num <= rules.size() && num > 0) {
            cout << "Rule " << num << ": " << rules[num-1] << '\n';
        }
        else {
            cout << "Rule " << num << ": No such rule\n";
        }
    }
}