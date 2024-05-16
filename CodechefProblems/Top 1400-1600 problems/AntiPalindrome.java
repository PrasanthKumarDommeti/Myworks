import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            String s = sc.next();

            int[] a = new int[23];
            for (int i = 0; i < n; i++) {
                a[s.charAt(i)-'a']++;
            }
            Arrays.sort(a);
            int odd =0;
            int even = 0;
            for (int i = 22; i >= 0; i--) {
                if (a[i]==0)
                    break;
                else if (a[i]%2 == 0)
                    even++;
                else 
                    odd++;
            }
            if (n%2 == 0){
                if (odd>0){
                    System.out.println(0);
                }else{
                    System.out.println(1);
                }
            }else{
                if (odd>1){
                    System.out.println(0);
                } else if (odd == 1) {
                    if (even == 0){
                        System.out.println(2);
                    }else{
                        System.out.println(1);
                    }
                }
            }
        }
	}
}