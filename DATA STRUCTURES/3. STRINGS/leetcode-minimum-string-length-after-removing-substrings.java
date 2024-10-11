import java.util.ArrayDeque;

class Solution {
    private int rec(String s) {
        if (s.length() == 0) {
            return 0;
        }

        ArrayDeque<String> deque = new ArrayDeque<>();
        for (char c : s.toCharArray()) {

            if (deque.size() > 2) {

            }
        }
        return deque.size();
    }

    public int minLength(String s) {
        return rec(s);
    }
}

class Main {
    public static void main(String[] args) {
        Solution solObj = new Solution();
        int res = solObj.minLength("ABFCACDB");
        System.out.println(res);
    }
}