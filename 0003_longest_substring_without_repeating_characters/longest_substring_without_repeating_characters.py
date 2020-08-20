class Solution():
    def lengthOfLongestSubstring(s):
        st = 0
        unChar = {}
        max_ans = 0
        ll = len(s)
        for i in range(ll):
            if(s[i] in unChar and unChar[s[i]] >= st):
                st = unChar[s[i]] + 1
            else:
                max_ans = max(max_ans, i - st + 1)
            unChar[s[i]] = i
            
        return max_ans
        
