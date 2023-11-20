#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<string> split(const string &);

int maximumDraws(int n)
{
    // 1 -> 2, 2 -> 3, 3 -> 4
    return n + 1;
}

int main()
{
    string line;
    getline(cin, line);
    int testCases = stoi(line);

    // go over the test cases
    while (testCases--)
    {
        getline(cin, line);
        vector<string> input = split(line);

        // Update here
        int n = stoi(input[0]);
        int output = maximumDraws(n);

        cout << output << endl;
    }

    return 0;
}

vector<string> split(const string &str)
{
    vector<string> words;
    istringstream iss(str);
    string word;

    while (iss >> word)
    {
        words.push_back(word);
    }

    return words;
}
