#Devin Longtree [Palindrome]

text = input("Give me a word: ")
rev_text = text[::-1]
if text == rev_text:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
