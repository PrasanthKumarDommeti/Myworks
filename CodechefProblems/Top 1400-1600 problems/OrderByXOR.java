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
            long a = sc.nextLong();
            long b = sc.nextLong();
            long c = sc.nextLong();
            System.out.println(solve(a, b, c));
        }
    }
    static long solve(long a, long b, long c) {
        long ans = 0;
        if (a > b) {
            ans = biggest_bit(a, b);
        }
        if (b > c) {
            ans |= biggest_bit(b, c);
        }
        if ((a ^ ans) < (b ^ ans) && (b ^ ans) < (c ^ ans)) return ans;
        return -1;
    }
    
    static long biggest_bit(long a, long b) {
        for (int i = 29; i >= 0; i--) {
            long val = 1 << i;
            if ((val & a) > 0 && (val & b) == 0) return val;
        }
        return 0;
    }
}