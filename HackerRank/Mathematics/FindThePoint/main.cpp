#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<string> split(const string &);

vector<int> findPoint(int px, int py, int qx, int qy)
{
    vector<int> result;
    int rx = qx - px + qx;
    int ry = qy - py + qy;

    result.push_back(rx);
    result.push_back(ry);
    return result;
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

        // 0 0 1 1
        int px = stoi(input[0]);
        int py = stoi(input[1]);
        int qx = stoi(input[2]);
        int qy = stoi(input[3]);

        // Update here
        vector<int> output = findPoint(px, py, qx, qy);

        for (size_t i = 0; i < output.size(); i++)
        {
            cout << output[i];

            if (i != output.size() - 1)
            {
                cout << " ";
            }
        }

        cout << "\n";
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
