import java.util.Scanner;

public class numeralCalculations {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            a[i] = scanner.nextInt();
        }
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += a[i];
            if (sum < 0) {
                sum = 0;
            }
        }
        System.out.println(sum);
    }
}

//input
//6
//1 -2 3 -8 5 1

//output
//6