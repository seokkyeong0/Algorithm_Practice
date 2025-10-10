#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int seminar[7] = { 0 };

    for (int i = 0; i < 7; i++) {
        string s;
        int score;
        cin >> s >> score;

        if (s == "Algorithm") seminar[0] = score;
        else if (s == "DataAnalysis") seminar[1] = score;
        else if (s == "ArtificialIntelligence") seminar[2] = score;
        else if (s == "CyberSecurity") seminar[3] = score;
        else if (s == "Network") seminar[4] = score;
        else if (s == "Startup") seminar[5] = score;
        else if (s == "TestStrategy") seminar[6] = score;
    }

    int max = seminar[0], max_idx = 0;
    for (int i = 0; i < 7; i++) {
        if (seminar[i] > max) {
            max = seminar[i];
            max_idx = i;
        }
    }

    if (max_idx == 0) cout << "Algorithm";
    else if (max_idx == 1) cout << "DataAnalysis";
    else if (max_idx == 2) cout << "ArtificialIntelligence";
    else if (max_idx == 3) cout << "CyberSecurity";
    else if (max_idx == 4) cout << "Network";
    else if (max_idx == 5) cout << "Startup";
    else if (max_idx == 6) cout << "TestStrategy";
}