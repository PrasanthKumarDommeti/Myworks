import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        int t= sc.nextInt();
        while(t-->0){
            int n= sc.nextInt();
            int x= sc.nextInt();
            int[] a = new int[n];
            int even = 0;
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
                if ((a[i]&1)==0){
                    even++;
                }
            }
            
            if ((x&1)==0){
                if (even==n){
                    System.out.println(-1);
                }else{
                    System.out.println(even);
                }
            }else{
                System.out.println((int)Math.ceil((double) even/2));
            }
        }
	}
}
