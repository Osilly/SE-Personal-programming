//最费时的函数是欧拉筛筛出素数的过程，时间复杂度为O(n)
//如果n过大的情况，可以使用Min_25筛进行优化，复杂度为O( n^(3/4)/log(n) )

import java.util.Arrays;

class Solution {
    int[] prime;

    public int countPrimes(int n) {
        if (n < 2)
            return 0;

        prime = new int[n];
        int pn = 0;

        boolean[] mark = new boolean[n];
        Arrays.fill(mark, true);
        mark[0] = false;
        mark[1] = false;

        for (int x = 2; x < n; x++) {
            if (mark[x] == true) {
                prime[pn++] = x;
            }
            int pi = 0;
            while (pi < pn && prime[pi] * x < n) {
                mark[prime[pi] * x] = false;
                pi++;
            }
        }

        return pn;
    }
}

public class primeNumber {
    public static void main(String args[]) {
        Solution solution = new Solution();
        int ans = solution.countPrimes(20000);
        for (int i = 0; i < ans; i++) {
            System.out.print(solution.prime[i] + " ");
            if ((i + 1) % 5 == 0) {
                System.out.println();
            }
        }
    }
}