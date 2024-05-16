import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
    public static void main(String[] args) throws java.lang.Exception
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            long val = 1;
            System.out.print(val + " ");
            for (int i = 0; i < n; i++) {
                System.out.print(val + " ");
                val *= 2;
            }
            System.out.println();
        }

    }
}