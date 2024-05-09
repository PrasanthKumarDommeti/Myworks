import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		while(a-->0)
		{
		    int seqno = sc.nextInt();
		    int swaps = sc.nextInt();
		    int motus=0,tomus=0;
            //Here we can use the 2 pointer approaches to solve the problem
		    ArrayList<Integer> motu=new ArrayList<>();
            ArrayList<Integer> tomu=new ArrayList<>();
		    for(int i=0;i<seqno;i++)
		    {
		        if(i%2==0)
		        {
		            int x = sc.nextInt();
		            motu.add(x);
		        }
		        else{
		            int y = sc.nextInt();
		            tomu.add(y);
		        }
		       
		    }
		    Collections.sort(motu);
		    Collections.sort(tomu);
		    int s = motu.size()-1;
		    int v =0;
		    while(swaps!=0)
		    {
		        if(motu.get(s)>tomu.get(v)){
		            
		        // 1 pointer will be end of the motu list and another one is tomu starting list
		        int h = tomu.get(v);
		        int y = motu.get(s);
		        tomu.set(v,y);
		        motu.set(s,h);
		        swaps-=1;
		        s--;
		        v++;}
		        else break;
		        
		    }
		    for(int m =0 ;m<motu.size();m++)
		    {
		        motus+=motu.get(m);
		    }
		    for(int n =0;n<tomu.size();n++)
		    {
		        tomus+=tomu.get(n);
		    }
		    if(tomus>motus)
		    {
		        System.out.println("YES");
		    }
		    else System.out.println("NO");
		}

	}
}
