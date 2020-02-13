# Note: A palindrome is word, phrase,
# or sequence that reads the same backward as forward,
# e.g., madam or nurses run.

def palindromeCheck(s):
    return s == s[::-1]


print(palindromeCheck('madam'))