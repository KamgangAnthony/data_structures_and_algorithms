class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        print(f"s : {s}")
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            print(f"i : {i} , j : {j}")
        return True


s = "A man, a plan, a canal: Panama"
our_solution = Solution()
print(our_solution.isPalindrome(s))
