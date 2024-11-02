def palindrome(word):
    if word == word[::-1]:
        return True
    else: return False

word = input('Enter word: ')
print(palindrome(word))