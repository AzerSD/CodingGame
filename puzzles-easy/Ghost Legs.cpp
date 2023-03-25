#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int w, h;
    cin >> w >> h;
    cin.ignore();

    vector<string> input(h);
    for (int i = 0; i < h; i++)
        getline(cin, input[i]);

    vector<vector<char>> matrix(h, vector<char>(w));
    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++)
            matrix[i][j] = input[i][j];

    vector<char> top_labels;
    for (int i = 0; i < w; i += 3)
        top_labels.push_back(input[0][i]);

    vector<char> bottom_labels;
    for (int i = 0; i < w; i += 3)
        bottom_labels.push_back(input[h-1][i]);


    for (int i = 0; i < top_labels.size(); i++) {
        int x = i * 3;
        int y = 1;
        while (y < h-1) {
            if (x >= 0 && input[y][x-1] == '-')
                x -= 3;
            else if (x < w-1 && input[y][x+1] == '-')
                x += 3;
            y++;
        }
        cout << top_labels[i] << bottom_labels[x/3] << endl;
    }

    return 0;
}

