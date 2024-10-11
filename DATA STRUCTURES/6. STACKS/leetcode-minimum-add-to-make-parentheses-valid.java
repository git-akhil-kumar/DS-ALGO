
import java.util.Stack;

class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Integer> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                stack.push(1);
            } else if (ch == ')' && !stack.isEmpty() && stack.peek() == 1) {
                stack.pop();
            } else {
                stack.push(2);
            }
        }
        return stack.size();
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("------------------------------");
        Solution sol = new Solution();
        int ans = sol.minAddToMakeValid("(((");
        System.out.println(ans);

    }
}