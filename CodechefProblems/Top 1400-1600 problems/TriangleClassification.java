import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sid = scanner.nextInt(); // Get input for sid
        int T = scanner.nextInt(); // Get input for T (number of test cases)
        for (int tc = 0; tc < T; tc++) {
            int x1 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y2 = scanner.nextInt();
            int x3 = scanner.nextInt();
            int y3 = scanner.nextInt();
            double d1 = dis(x1, y1, x2, y2);
            double d2 = dis(x1, y1, x3, y3);
            double d3 = dis(x2, y2, x3, y3);
            String t = "";
            String a = "";
            double M = Math.max(Math.max(d1, d2), d3);
            double sumd = d1 + d2 + d3;
            if (d1 != d2 && d2 != d3 && d1 != d3) {
                t = "Scalene";
            } else {
                t = "Isosceles";
            }
            if (sid == 1) {
                System.out.println(t + " triangle");
            } else if (sid == 2) {
                if (M == sumd - M) {
                    a = "right";
                } else if (M > sumd - M) {
                    a = "obtuse";
                } else {
                    a = "acute";
                }
                System.out.println(t + " " + a + " triangle");
            }
        }
    }

    static double dis(int x1, int y1, int x2, int y2) {
        return Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2);
    }
}
