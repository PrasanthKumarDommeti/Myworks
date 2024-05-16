import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int t,i,j,k,l,m,n;
		Scanner sc = new Scanner(System.in);
		t = sc.nextInt();
		while(t-->0){
		    n = sc.nextInt();
		    j = 1;
		    for(i = 1; i<=n; i++){
		        if(i%2 == 0) System.out.print(2*(i-1)+" ");
		        else System.out.print(i+" ");
		    }
		    System.out.println();
		}
	}
}
