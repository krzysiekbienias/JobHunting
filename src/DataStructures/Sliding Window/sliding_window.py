def longestSubstringWithoutRepeatingCharacters(a_str):
    """
    Description
    -----------
    This function seeks the longest substring without repeating character


    Parameters
    ----------
    a_str

    Returns int
    -------

    """
    left=0
    right=0
    char_map={}
    res=0
    while right<len(a_str):
        r=a_str[right]
        if r in char_map:
            char_map[r]+=1
        else:
            char_map[r] = 1
        while char_map[r]>1:
            l=a_str[left]
            char_map[l]-=1
            left+=1
        res=max(res,right-left+1)
        right+=1
    return res

if __name__=="__main__":
   longestSubstringWithoutRepeatingCharacters(a_str="abcabcbb")
