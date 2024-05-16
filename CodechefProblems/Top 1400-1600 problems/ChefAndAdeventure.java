import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            int n = sc.nextInt(), m = sc.nextInt(), x = sc.nextInt(), y = sc.nextInt();
            if((n==1 && m==1)||(m==2 && n==2))
                System.out.println("Chefirnemo");
            else if((((n-1)%x==0) && ((m-1)%y==0) && n-1>=0 && m-1>=0)||(((n-2)%x==0) && ((m-2)%y==0)&& n-2>=0 && m-2>=0))
                System.out.println("Chefirnemo");
            else
                System.out.println("Pofik");
        }
	}
}
