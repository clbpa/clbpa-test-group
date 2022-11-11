#include <iostream>
#include <fstream>

using namespace std;

string toString(int n) {
  string s = "";
  while (n > 0) {
    s = char(n % 10 + '0') + s;
    n /= 10;
  }
  return s;
}

string compress(string s) {
  string kq = "";
  int k = 1;
  s = s + " ";
  for (int i = 0; i < s.length() - 1; i++)
    if (s[i] == s[i + 1]) k++;
    else {
      if (k > 1)
        kq = kq + toString(k);
      kq = kq + s[i];
      k = 1;
    }
  return kq;
}

int main() {
  ifstream inp("BAI-3.IN");

  string s;
  inp >> s;
  inp.close();

  ofstream out("BAI-3.OUT");

  out << compress(s);
  out.close();
  return 0;
}
