#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<string> split(const string &);

int handshake(int area, int trianglebase)
{
    return ceil(2.0 * area / trianglebase);
}

int main()
{
    string line;

    getline(cin, line);
    vector<string> input = split(line);
    int area = stoi(input[0]);
    int trianglebase = stoi(input[1]);

    // Update here
    int output = handshake(area, trianglebase);

    cout << output << endl;

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
