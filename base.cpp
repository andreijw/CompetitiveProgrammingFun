#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<string> split(const string &);

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
    vector<string> output = input;

    for (size_t i = 0; i < output.size(); i++)
    {
      cout << output[i];

      if (i != output.size() - 1)
      {
        cout << " ";
      }
    }

    cout << endl;
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
