// url :- https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import java.util.PriorityQueue;

class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        long ans = 0;
        for (int num : nums) {
            pq.add(num);
        }

        while (!pq.isEmpty() && k > 0) {
            int curr = pq.poll();
            double curr_double = curr / 3.0;
            pq.add((int) Math.ceil(curr_double));
            ans += curr;
            --k;
        }
        return ans;
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("-----------------");
        Solution sol = new Solution();
        int[] nums = { 10, 10, 10, 10, 10 };
        long ans = sol.maxKelements(nums, 5);
        System.out.println(ans);
    }
}
