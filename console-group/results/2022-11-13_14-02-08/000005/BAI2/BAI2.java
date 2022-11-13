import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class BAI2 {
  static boolean isPrime(int n) {
    if (n <= 1)
      return false;

    for (int i = 2; i < n; i++)
      if (n % i == 0)
        return false;

    return true;
  }

  public static void main(String args[]) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    
    int n = Integer.parseInt(reader.readLine());
    if (isPrime(n)) {
      System.out.print("true");
    } else {
      System.out.print("false");
    }
  }
}
