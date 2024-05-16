import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
    static final long MODULO = 1000000007;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        while (testCases-- > 0) {
            int n = sc.nextInt();
            int x = sc.nextInt();
            System.out.println((x * power(n - 1)) % MODULO);
        }
    }


    private static long power(long n) {
        long result = 1;
        long x = 2;
        while (n > 0) {
            if (n % 2 == 1) {
                result = (result * x) % MODULO;

            }
            n /= 2;
            x = (x * x) % MODULO;
        }
        return result;
    }
}