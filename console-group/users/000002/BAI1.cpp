#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  
  int gdc = __gcd(a, b);
  int lcm = (a * b) / gdc;
  
  cout << gdc << " " << lcm;
  return 0;
}
