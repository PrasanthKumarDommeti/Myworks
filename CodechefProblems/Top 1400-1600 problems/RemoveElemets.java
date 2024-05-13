
import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
		    int n = sc.nextInt(), k = sc.nextInt();
		    long max = Long.MIN_VALUE;
		    long min = Long.MAX_VALUE;
		    long[] arr = new long[n];
		    for(int i=0;i<n;i++)
		    {
		        arr[i] = sc.nextLong();
		        if(arr[i] > max) max = arr[i];
		        if(arr[i] < min) min = arr[i];
		    }
		    if(((min+max) <= k) || n==1) System.out.println("YES");
		    else System.out.println("NO");
		    
		}
	}
}