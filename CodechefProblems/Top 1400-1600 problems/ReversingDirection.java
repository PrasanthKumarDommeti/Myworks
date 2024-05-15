import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
    public static void main (String[] args) throws java.lang.Exception
    {
        FastReader sc = new FastReader();
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            ArrayList<ArrayList<String>> list = new ArrayList<>();
            for(int i=0;i<n;i++){
                String temp = sc.nextLine();
                ArrayList<String> l = new ArrayList<>();
                for(String str : temp.split(" ")){
                    l.add(str);
                }
                list.add(l);
            }
            String prev = "Begin";
            for(int i=n-1;i>=0;i--){
                    if(prev == "Begin"){
                        String temp = list.get(i).get(0);
                        list.get(i).set(0,prev);
                        prev = temp;
                    }else{
                        if(prev.equals("Right")){
                            String temp = list.get(i).get(0);
                            list.get(i).set(0,"Left");
                            prev = temp;
                        }else{
                            String temp = list.get(i).get(0);
                            list.get(i).set(0,"Right");
                            prev = temp;
                        }
                    }
            }
            for(int i =n-1;i>=0;i--){
                for(int j=0;j<list.get(i).size();j++) {
                   System.out.print(list.get(i).get(j)+" ");
                }
                System.out.println();
            }

        }

    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}