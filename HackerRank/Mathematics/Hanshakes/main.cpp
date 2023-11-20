#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<string> split(const string &);

int handshake(int n)
{
    // 1 -> 0, 2 -> 1, 3 -> 3, 4 -> 6
    int handshakes = 0;

    for (int i = n - 1; i > 0; i--)
    {
        handshakes += i;
    }

    return handshakes;
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
        int input = stoi(line);

        // Update here
        int output = handshake(input);

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
