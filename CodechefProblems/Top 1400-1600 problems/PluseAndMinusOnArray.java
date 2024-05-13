import java.util.*;

public class Main {
	public static void main (String[] args)
	{
        Scanner input = new Scanner(System.in);
        int  t = input.nextInt();
        input.nextLine();
        while(t-- > 0) {
            int n = input.nextInt();
            int  A[] = new int[n];
            long sum = 0;
            int mn = 1000000000, mx = -1;
            for(int i = 0; i < n; i++) {
                A[i] = input.nextInt();
                A[i] = Math.abs(A[i]);
                if(i % 2 == 0) {
                    sum += A[i];
                    mn = Math.min(mn, A[i]);
                }
                else {
                    sum -= A[i];
                    mx = Math.max(mx, A[i]);
                } 
            }
            if(mn < mx) {
                sum -= (mn*2);
                sum += (mx*2);
            }
            System.out.println(sum);
        }
	}
}
