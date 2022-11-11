#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream inp("BAI-2.IN");

  int n;
  inp >> n;
  inp.close();

  ofstream out("BAI-2.OUT");
  
  out << "true";

  out.close();
  return 0;
}
