# User function Template for python3

class Solution:
    def longestCommonPrefix(self, str1, str2):
        # code here
        res1 = [str1[i: j] for i in range(len(str1))
                for j in range(i + 1, len(str1) + 1)]

        res2 = [str2[i: j] for i in range(len(str2))
                for j in range(i + 1, len(str2) + 1)]

        maxstring = max((list(set(res1).intersection(res2))), key=len)
        first_index = str1.find(maxstring)
        last_index = first_index + len(maxstring) - 1

        return str(first_index) + str(last_index)

    def longestCommonPrefixAlternative(self, str1, str2):
        n = len(str1)
        i = 0
        indexes = list()
        while i < n and str1[i] == str2[i]:
            i = i + 1



# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ob = Solution()
        ans = ob.longestCommonPrefix(str1, str2)
        if ans[0] == -1:
            print(-1)
        else:
            print(ans[0], ans[1])

# } Driver Code Ends