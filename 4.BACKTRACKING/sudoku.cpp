#include<bits/stdc++.h>
using namespace std;

bool isValid(int x, int y, char ch, vector<vector<char> > &board) {
    for(int i=0;i<9;i++){
        if(board[i][y] == ch || board[x][i] == ch){
            return false;
        }
    }
    int X = (x/3) * 3;
    int Y = (y/3) * 3;
    
    for(int row = X; row < X+3; ++row){
        for(int col = Y; col < y+3; ++col){
            if(board[row][col] == ch){
                return false;
            }
        }
    }
    return true;
}

bool dfs(vector<vector<char> > &board, int x, int y){
    if(x == 9){
        return true;
    }
    if(y == 9) {
        return dfs(board, x+1, 0);
    }
    if(board[x][y] != '.'){
        return dfs(board, x, y+1);
    }
    for(char ch = 1; ch <= 9; ch++){
        if(isValid(x, y, ch, board)){
            board[x][y] = ch;
            if(dfs(board, x, y+1)){
                return true;
            }
            board[x][y] = '.';
        }
    }
    return false;
}
solveSudoku(vector<vector<char> > &board) {
    dfs(board, 0, 0);
}


int main() {
    vector<vector<char> > board = {"53..7....", "6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"};
    vector<vector<char> > ans = solveSudoku(board);
    return 0;
}