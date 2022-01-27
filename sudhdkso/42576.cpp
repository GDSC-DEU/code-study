#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";
	unordered_map<string, int> hash;

	for (int i = 0;i < participant.size();i++) {
		if (hash.end() == hash.find(participant[i]))
			hash.insert({ participant[i], 1 });
		else
			hash[completion[i]]++;
	}


	for (int i = 0;i < completion.size();i++) {
		hash[completion[i]]--;
		if (hash[completion[i]] <= 0) {
			answer = completion[i];
			break;
		}

	}
	return answer;
}