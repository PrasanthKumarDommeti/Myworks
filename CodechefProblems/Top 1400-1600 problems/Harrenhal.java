import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0)
		{
		    String s=sc.next();
		    StringBuffer sb=new StringBuffer(s);
		    if(s.indexOf('a')==-1||s.indexOf('b')==-1)
		    System.out.println("1");
		    else
		    {
		     if(s.equals(String.valueOf(sb.reverse())))
		      System.out.println("1");
		     else
		     System.out.println("2");
		    }
		        
		    }
	}
}