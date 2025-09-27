#include <iostream>
#include <string>
#include <list>
using namespace std;

int main(void) {
    int m;
    string s;
    list<char> L;

    // 초기 문자열 입력
    cin >> s;
    for (auto c : s) L.push_back(c);

    // 커서 초기 위치 설정
    list<char>::iterator cursor = L.end();

    // 명령어 횟수 입력
    cin >> m;
    for (int i = 0; i < m; i++) {
        char c1, c2;

        // 명령어 입력
        cin >> c1;

        if (c1 == 'L') {
            if (cursor != L.begin()) 
                cursor--;
        }
        else if (c1 == 'D') {
            if (cursor != L.end())
                cursor++;
        }
        else if (c1 == 'B') {
            if (cursor != L.begin()) 
                cursor = L.erase(--cursor);
        }
        else if (c1 == 'P') {
            cin >> c2;
            L.insert(cursor, c2);
        }
    }

    for (auto c : L) cout << c;
}