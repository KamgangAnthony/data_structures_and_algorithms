
def is_subsequence(s: str, t: str):
    """
    Example 4: 392. Is Subsequence.

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    x = 0
    y = 0
    for letter in t:
        if letter == s[x]:
            if y == len(s) - 1:
                return True
            x += 1
            y += 1
    return False

print(is_subsequence("ce", "abcde"))

"""My pseudo code
Take the lenght of the string s
x = y = 0
Have a variable x that store the index at
which I am on the string s
Have a variable y that verifies if we have 
reached the end of the string s
go through the string t letter by letter
If the t letter == the s letter
	increment x
	increment y
	check if y == lenght of string s - 1:
		return True
return False"""