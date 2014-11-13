def palindrome_test(word):
    if word == word[::-1]:
        return "True"
    else:
        return "False"

word = input("Check if palindrome: ")
result = palindrome_test(word)
print(result)
