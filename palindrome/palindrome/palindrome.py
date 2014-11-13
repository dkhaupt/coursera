def palindrome_test(word):

    return word == word[::-1]

word = input("Check if palindrome: ")
print(palindrome_test(word))
