class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def dfs(depth, val):
            if depth == 0:
                return 1
            
            result = 0
            for i in range(val, 0, -1):
                result += dfs(depth-1, i)
            
            return result
        
        return dfs(n, 5)
                