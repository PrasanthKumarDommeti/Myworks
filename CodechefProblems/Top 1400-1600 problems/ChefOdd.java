import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T>=1){
		    long n = sc.nextLong();
		    long k = sc.nextLong();
		    long odd;
            if (n % 2 == 1) {
                odd = (n / 2) + 1;
            } else {
                odd = n / 2;
            }
            if (n < 2 * k) {
                System.out.println("NO");
            } else if (k % 2 == odd % 2) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
		    T--;
		}
	}
}