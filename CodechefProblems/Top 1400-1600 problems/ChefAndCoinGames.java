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
            //Power is even it can be misha else it can be chef
            if(n%6==0)
            {
                System.out.println("Misha");
            }
            else{
                System.out.println("Chef");
            }
        }
	}
}
