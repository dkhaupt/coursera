def palindrome_test(word):
    #tests to see if provided word is a palindrome
    copy = word[:]
    return word == word[::-1]

word = input("Check if palindrome: ")
print(palindrome_test(word))