#include <iostream>

using namespace std;

int gcdF(int x, int y) {
  if (y == 0) return x;
  
  return gcdF(y, x % y);
}

int main() {
  int a, b;
  cin >> a >> b;
  
  int gcd = gcdF(a, b);
  int lcm = (a * b) / gcd;
  
  cout << gcd << " " << lcm;
  return 0;
}

