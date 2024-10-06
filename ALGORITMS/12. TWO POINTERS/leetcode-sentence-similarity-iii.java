// url :- https://leetcode.com/problems/sentence-similarity-iii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Solution {
  public boolean areSentencesSimilar(String sentence1, String sentence2) {
    final int n1 = sentence1.length();
    final int n2 = sentence2.length();
    if (n1 == n2) {
      return sentence1.equals(sentence2);
    }
    if (n1 > n2) {
      return areSentencesSimilar(sentence2, sentence1);
    }

    String[] array1 = sentence1.split(" ");
    String[] array2 = sentence2.split(" ");

    HashSet<String> set1 = new HashSet<>();
    HashSet<String> set2 = new HashSet<>();

    for (String word : array1) {
      set1.add(word);
    }
    for (String word : array2) {
      set2.add(word);
    }
    boolean prefixCase = true, suffixCase = true;
    for (int i = 0; i < array1.length; i++) {
      if (!array1[i].equals(array2[i])) {
        prefixCase = false;
        break;
      }
    }

    if (prefixCase) {
      return true;
    }
    int n = array2.length - 1;
    for (int i = array1.length - 1; i >= 0; i--) {
      if (!array1[i].equals(array2[n])) {
        suffixCase = false;
        break;
      }
      n--;
    }
    if (suffixCase) {
      return true;
    }
    int half = 0;
    while (array1[half].equals(array2[half]))
      ++half;

    n = array2.length - 1;
    for (int i = array1.length - 1; i >= half; i--) {
      if (!array1[i].equals(array2[n])) {
        return false;
      }
      --n;
    }
    return true;
  }
}

class Main {

  public static void main(String[] args) {
    Solution sol = new Solution();
    boolean res = true;
    ArrayList<ArrayList<String>> testcases = new ArrayList<>();
    testcases.add(new ArrayList<>(Arrays.asList("My name is Haley", "My Haley")));
    testcases.add(new ArrayList<>(Arrays.asList("A B C D B B", "A B B")));
    testcases.add(new ArrayList<>(Arrays.asList("A a a a A A A", "A A a a a")));
    testcases.add(new ArrayList<>(Arrays.asList("z z z z", "zz z")));
    testcases.add(new ArrayList<>(Arrays.asList("A a a", "Aa a")));
    testcases.add(new ArrayList<>(Arrays.asList("hello racecar", "hello racecar acecar")));

    for (ArrayList<String> testcase : testcases) {
      res = sol.areSentencesSimilar(testcase.get(0), testcase.get(1));
      System.out.println(testcase.get(0) + " | " + testcase.get(1) + " | " + res);
    }
  }
}

/**
 * 3 cases :-
 * 1. entire smaller should be prefix
 * 2. entire smaller should be the suffix
 * 3. smaller should be prefix + suffix
 */