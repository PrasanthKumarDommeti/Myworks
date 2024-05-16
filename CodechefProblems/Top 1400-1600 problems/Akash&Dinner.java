import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
        public FastReader()
        {
            br=new BufferedReader(new InputStreamReader(System.in));
        }
        String next()throws Exception
        {
            while(st==null || !st.hasMoreElements())
                st=new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt()throws Exception
        {
            return Integer.parseInt(next());
        }
        long nextLong()throws Exception
        {
            return Long.parseLong(next());
        }
    }
	public static void main (String[] args) throws java.lang.Exception
	{
		FastReader sc = new FastReader();
		int n=sc.nextInt();
		while(n-->0)
		{
		    int sizA=sc.nextInt(),reqDish=sc.nextInt(),j=0;
		    long time=0;
		    int []A=new int[sizA];
		    int []B=new int[sizA];
		    for(int i=0;i<2*sizA;i++)
		    {
		        if(i<sizA)
		            A[i]=sc.nextInt();
		        else
		        {
		            B[j]=sc.nextInt();
		            j+=1;
		        }
		    }
		    HashMap<Integer,Integer>map=new HashMap<>();
		    for(int i=0;i<sizA;i++)
		    {
		        if(map.containsKey(A[i]))
		        {
		            int val=map.get(A[i]);
		            if(B[i]<val)
		                map.replace(A[i],B[i]);
		        }
		        else
		        {
		            map.put(A[i],B[i]);
		        }
		    }
		    if(map.size()<reqDish)
		        System.out.println(-1);
		    else
		    {
		        Vector<Integer>sorArr = new Vector<>();
		        for(Map.Entry<Integer,Integer>mm:map.entrySet())
		        {
		            sorArr.add(mm.getValue());
		        }
		        Collections.sort(sorArr);
		        for(int i=0;i<reqDish;i++)
		            time+=sorArr.get(i);
		        System.out.println(time);
		    }
		}
	}
}