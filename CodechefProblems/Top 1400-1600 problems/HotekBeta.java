import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        while(a-->0)
        {
            int room = sc.nextInt();
            int count=0,c=0;
            // Arrival & Vacate time of the rooms
            int Ari[] = new int[room];
            int vac[] = new int[room];
            for(int i=0;i<room;i++)
            {
                Ari[i] = sc.nextInt();
            }
            for(int j=0;j<room;j++)
            {
                vac[j] = sc.nextInt();
            }
            Arrays.sort(Ari);
            Arrays.sort(vac);
            for(int k=0;k<room;k++)
            {
                // If arrival time is not greater than vacate then moves into the vacation time incrementation
                if(Ari[k]<vac[c])
                {
                    count+=1;
                }
                else c++;
            }
            System.out.println(count);
            
        }
	}
}
