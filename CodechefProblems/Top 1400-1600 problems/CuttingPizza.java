import java.util.Scanner;

public class Main {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); 
        while (t-- > 0) {
            int n = scanner.nextInt(); 
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            int[] diff = new int[n];
            for (int i = 1; i < n; i++) {
                diff[i] = a[i] - a[i - 1];
            }
            diff[0] = 360 - a[n - 1] + a[0];
            int hcf = gcd(diff[0], diff[1]);
            for (int i = 2; i < n; i++) {
                hcf = gcd(hcf, diff[i]);
            }
            int res = 0;
            for (int i : diff) {
                res += (i / hcf) - 1;
            }
            System.out.println(res);
        }
    }
}
