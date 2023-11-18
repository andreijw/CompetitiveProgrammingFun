#include <bits/stdc++.h>

using namespace std;

int main(){
  int tc;
  cin >> tc;

  while (tc--){
    int n,m,i,j;
    cin >> n >> m >> i >> j;

    int x1,y1,x2,y2,d1,d2;

    d1 = abs(1-i) + abs(1-j);
    d2 = abs(n-i) + abs(m-j);

    if (d1 > d2){
      x1 = 1;
      y1 = 1;
      x2 = n;
      y2 = m;
    }
    else{
      x1 = 1;
      y1 = m;
      x2 = n;
      y2 = 1;
    }
    
    cout << x1 << " " << y1 << " " << x2 << " " << y2 << "\n";
  }
}
