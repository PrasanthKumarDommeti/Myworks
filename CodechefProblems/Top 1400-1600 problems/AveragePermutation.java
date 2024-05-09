import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		while(a-->0){
		    int mi = sc.nextInt();
		    int arr[] = new int[mi];
		    int s = mi;
            //The for loop can be used to find the optimal permutations in a manner
		    for(int j=0;j<mi/2;j++)
		    {
		        arr[j] = s;
		        arr[mi-j-1] = s-1;
		        s= s-2;
		    }
            //The arrangement of the first element should be changeed in a row
		    if(mi%2!=0)
		    {
		        arr[mi/2]=1;
		    }
		    for(int j=0;j<mi;j++)
		    {
		        System.out.print(arr[j]+" ");
		        
		    }
		    System.out.println("");
		    
		}

	}
}
