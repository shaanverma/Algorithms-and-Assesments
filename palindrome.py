def palindrome(word1, word2):
    return word1.upper() == word2.upper()[::-1]


#Testcases
a = palindrome('shaan','bob')
b = palindrome('racecar','racecar')
c = palindrome('vvv','vvv')

print(a,b,c)
