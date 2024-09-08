class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: # prevent empty list
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]
        print("current prefix: ", prefix)
        # Compare the prefix with each string in the array
        for string in strs[1:]:
            
            while prefix and string[:len(prefix)] != prefix:
            
                # Shorten the prefix
                prefix = prefix[:-1] # 將會一個字一個字減少
                print(prefix)
            
            # If there's no common prefix, return an empty string
            if not prefix:
                return ""
        
        return prefix

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print( Solution().longestCommonPrefix(["dog","racecar","car"]) )