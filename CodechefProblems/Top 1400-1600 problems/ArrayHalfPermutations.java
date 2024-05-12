
import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
    public static void main(String[] args) throws java.lang.Exception
    {
        // your code goes here
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();
        while (t-- > 0) {
            int n = sc.nextInt();
            long arr[] = new long[2 * n];
            long j = 0;
            long count = 0;
            for (int i = 0; i < 2 * n; i++) {
                arr[i] = sc.nextLong();
                if (arr[i] > n) {
                    count += n - i + j;
                    j++;
                }
            }
            System.out.println(count);
        }
        sc.close();
    }
}