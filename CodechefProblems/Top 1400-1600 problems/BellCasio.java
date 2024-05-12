import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef{
	public static void main (String[] args) throws java.lang.Exception{
	    Scanner in = new Scanner(System.in);
	    int t = in.nextInt();
	    while(t-->0){
	        long D = in.nextLong();
	        long d = in.nextLong();
	        long p = in.nextLong();
	        long q = in.nextLong();
	        long n = D/d;
	        long ans = d*(n*(2*p+(n-1)*q)/2);
	        ans+=(D-n*d)*(p+n*q);
	        System.out.println(ans);
	    }
	}
}