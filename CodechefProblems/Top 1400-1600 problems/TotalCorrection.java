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
            HashMap<String,Integer> ans = new HashMap<>();
            for (int i = 0; i < 3 * n; i++) {
                String s = sc.next();
                int a = sc.nextInt();
                if (ans.containsKey(s)){
                    ans.put(s,(ans.get(s)+a));
                }else{
                    ans.put(s,a);
                }
            }
            ArrayList<Integer> res = new ArrayList<>();
            for (String s : ans.keySet()) {
                res.add(ans.get(s));
            }
            Collections.sort(res);
            for (Integer re : res) {
                System.out.print(re + " ");
            }
            System.out.println();
        }
	}
}