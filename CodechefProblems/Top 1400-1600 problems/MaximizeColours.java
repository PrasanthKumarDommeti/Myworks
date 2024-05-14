import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
		    int arr[] = new int[3];
		    for(int i=0;i<3;i++)
		    {
		        arr[i]=sc.nextInt();
		    }
		    if(arr[0] ==1 && arr[1]==1 && arr[2]==1)
		    {
		        System.out.println(3);
		    }
		    else{
                int count=0;
                if (arr[0]!=0) count++;
                if (arr[1]!=0) count++;
                if (arr[2]!=0) count++;
                
                Arrays.sort(arr);
                if(arr[2] > 1 && arr[1]>1)
                {
                    arr[2]--;
                    arr[1]--;
                    count++;
                }
                if(arr[2] > 1 && arr[0]>1)
                {
                    arr[0]--;
                    arr[2]--;
                    count++;
                }
                if(arr[0] > 1 && arr[1]>1)
                {
                    arr[0]--;
                    arr[1]--;
                    count++;
                }
                System.out.println(count);		        
		    }
		}

	}
}
