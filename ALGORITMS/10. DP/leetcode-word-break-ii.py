# # url :- https://leetcode.com/problems/word-break-ii/
# Given a string s and a dictionary of strings wordDict, add spaces in s 
# to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
 
# Constraints:
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.

from typing import List, Optional

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s :
            return []
        
        wordSet = set(wordDict)
        del wordDict
        n = len(s)
        cache = {}

        def bottom_up_dp():
            table = [None] * (n+1)

            for i in range(n):
                for j in range(n):
                    pass


        def rec(i):
            if i in cache :
                return cache[i]
            
            if i == n :
                return [""]

            cur = ''
            sentences = []
            for j in range(i, n):
                cur += s[j]
                if cur in wordSet :
                    sub_sentences = rec(j+1)
                    for sentence in sub_sentences :
                        space = " " if sentence else ""
                        sentences.append(cur + space + sentence)
                         
            cache[i] = sentences
            return cache[i]

        return rec(0)
        
    

testcases = [["catsanddog",["cat","cats","and","sand","dog"]],["pineapplepenapple",["apple","pen","applepen","pine","pineapple"]],["catsandog",["cats","dog","sand","and","cat"]],["aaaaaaa",["aaaa","aa","a"]]]
results = [["cats and dog","cat sand dog"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"],[],\
           ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]]

sol = Solution()
for i, [sentence, dictionary] in enumerate(testcases) :
    sorted_res = sol.wordBreak(sentence, dictionary)
    sorted_res.sort()
    results[i].sort()
    print(sorted_res == results[i])

# print(sol.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))