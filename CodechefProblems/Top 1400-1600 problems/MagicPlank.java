import java.util.*;
class CodeChef
{
    static Scanner sc = new Scanner(System.in);
    public static void solve()
    {
        int n = sc.nextInt();
        String s = sc.next();
        int c = 0;
        for(int i = 0 ; i < n - 1 ; i++){
            if(s.charAt(i) != s.charAt(i+1)) {
                c++;
            }
        }

        if(c % 2 == 0){
            System.out.println(c / 2);
        } else {
            System.out.println((c + 1) / 2);
        }

    }
    public static void main (String[] args) throws java.lang.Exception
    {
        int t = sc.nextInt();
        while(t-->0)
            solve();
    }
}
