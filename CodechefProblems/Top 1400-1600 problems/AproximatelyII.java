import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
    public static void main(String[] args) throws java.lang.Exception
    {
        Scanner scn = new Scanner(System.in);
        int t = scn.nextInt();
        while (t-- > 0) {
            int n = scn.nextInt();
            int k = scn.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = scn.nextInt();
            }
            int min = Integer.MAX_VALUE;

            for (int i = 0; i < n - 1; i++) {
                for (int j = i + 1; j < n; j++) {
                    min = Math.min(min, Math.abs(arr[i] + arr[j] - k));
                }
            }
            System.out.print(min + " ");
            int cnt = 0;
            for (int i = 0; i < n - 1; i++) {
                for (int j = i + 1; j < n; j++) {
                    if ((Math.abs(arr[i] + arr[j] - k) == min)) {
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}