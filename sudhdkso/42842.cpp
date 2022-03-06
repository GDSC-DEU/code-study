#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int area = brown + yellow;
    int h=0;
    for (int w = area - 1; w > 0; w--) {
        if (area % w) continue;

        h = area / w;
        int y_area = (h - 2) * (w - 2);
        int b_area = area - y_area;

        if (y_area == yellow && b_area == brown) {
            answer.push_back(w);
            answer.push_back(h);
            return answer;
        }

    }
    
    return answer;
}