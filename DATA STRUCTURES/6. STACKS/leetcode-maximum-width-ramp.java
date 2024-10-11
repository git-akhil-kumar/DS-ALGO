// url :- https://leetcode.com/problems/maximum-width-ramp
// tough :- 2 pointers + preprocessing (stack)

import java.util.Stack;

class Solution {
    public int maxWidthRamp(int[] nums) {

        int res = Integer.MIN_VALUE;
        final int n = nums.length;
        int[] preprocessing = new int[n];
        preprocessing[n - 1] = nums[n - 1];

        Stack<Integer> stack = new Stack<>();

        for (int i = n - 2; i >= 0; --i) {
            if (!stack.empty() && nums[i] > stack.peek()) {

            }
        }
        int l = 0, r = 0;
        while (r < n) {
            while (l < r && nums[l] > preprocessing[r]) {
                ++l;
            }
            res = Math.max(res, r - l);
            ++r;
        }
        return res;
    }
}

class Hello {
    public static void main(String[] args) {
        System.out.println("------------------------");
        Solution sol = new Solution();
        int[] arr = { 9, 8, 1, 0, 1, 9, 4, 0, 4, 1 };
        final int ans = sol.maxWidthRamp(arr);
        System.out.println(ans);
    }
}