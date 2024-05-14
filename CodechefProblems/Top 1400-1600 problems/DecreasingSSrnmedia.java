
import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner s=new Scanner(System.in);
	   int t=s.nextInt();
	   while(t-->0){
	       int L=s.nextInt();
	       int R=s.nextInt();
	       System.out.println((R>=L*2)?-1:R);
	   }
	}
}