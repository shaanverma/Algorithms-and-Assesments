'''
Q: Create a function that takes two strings and returns True if either of the strings is a palindrome, else return False.
A palindrome is a word that is the same forwards and backwards. For example, "racecar" and "bob" are palindromes.
'''
def palindrome(word1, word2):
    return word1.upper() == word2.upper()[::-1]


#Testcases
a = palindrome('shaan','bob')
b = palindrome('racecar','racecar')
c = palindrome('vvv','vvv')

print(a,b,c)
