#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
  ifstream inp("BAI-1.IN");
  
  int a, b;
  
  inp >> a >> b;
  inp.close();
  
  ofstream out("BAI-1.OUT");
  
  int gdc = __gcd(a, b);
  int lcm = (a * b) / gdc;
  
  out << gdc << " " << lcm;
  out.close();
  return 0;
}
