class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Write a function that reverses a string. The input string is given as an array of characters s.

        You must do this by modifying the input array in-place with O(1) extra memory.



        Example 1:

        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        Example 2:

        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]


        Constraints:

        1 <= s.length <= 105
        s[i] is a printable ascii character.

        My old code
        Do not return anything, modify s in-place instead.

        my pseudo code (reasoning) :
        i = len(s) - 1
        j = 0
        create a copy h of s
        loop through i >= 0 or j <= i:
            make s elts go from first to last and equate
            each elt to a h elt going from last to first
            decrement i
            increment j
        delete h


        i = len(s) - 1
        j = 0
        h = s[:]
        while i >= 0:
            s[j] = h[i]
            i -= 1
            j += 1
        del h
        """

        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1