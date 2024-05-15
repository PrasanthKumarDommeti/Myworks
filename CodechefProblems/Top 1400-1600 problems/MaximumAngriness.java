import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
{		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0)
		{
		    long n=sc.nextLong();
		   long y=sc.nextLong();
		   long v1=y*(y+1)/2;
		  
		   if(n/2<=y)
		   {
		       System.out.println(n*(n-1)/2);
		   }else{
		       long v2=(n*(n-1)/2)-((n-y)*((n-y)-1)/2);
		       long v3=(n-(2*(y))-1)*y;
		       System.out.println(v1+v2+v3);
		   }
		    
		}
	}
}