import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
		    int n = sc.nextInt();
		    int pattern1=n*(n-1)*(n-1);
            int pattern2=n*(n-1)*(n-1);
            int pattern3=n*(n-1)*(n-2);
            int pattern4=n*(n-1)*(n-2)*(n-2);
            int pattern5=n*(n-1)*(n-2)*(n-2);
            System.out.println(pattern1+pattern2+pattern3+pattern4+pattern5);
		}

	}
}
