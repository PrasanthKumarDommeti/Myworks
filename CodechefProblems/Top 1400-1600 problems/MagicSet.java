import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
    private static int Power(int n){
        int ans=1,x=2;
        while(n!=0){
            if(n%2==1){
                ans=ans*x;
            }
            x*=x;
            n=n>>1;
        }
        return ans;
    }
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
		    int n=sc.nextInt();
		    int m=sc.nextInt();
		    int cnt=0;
		    for(int i=0;i<n;i++){
		        int value=sc.nextInt();
		        if(value%m==0)
		            cnt++;
		    }
		    System.out.println(Codechef.Power(cnt)-1);
		    
		}
	}
}
