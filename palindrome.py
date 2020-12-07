# 1st method using join
# word = input('Enter your word: ')
# reversedWord = ''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
#
# if word == reversedWord:
#     print(f'{word} = {reversedWord}')
#     print("It is a palindrome!")
# else:
#     print("It is not a palindrome.")

#  2nd method using slicing
word = input('Enter your word: ')
reversedWord = word[::-1]

if word == reversedWord:
    print(f'{word} = {reversedWord}')
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")

#  using loop
# word = input('Enter your word: ')
# reversedWord = ""
#
# index = len(word) # calculate length of string and save in index
# while index > 0:
#     reversedWord = reversedWord + word[index - 1] # save the value of str[index-1] in reverseWord
#     index = index - 1 # decrement index
#
# if word == reversedWord:
#     print(f'{word} = {reversedWord}')
#     print("It is a palindrome!")
# else:
#     print("It is not a palindrome.")
