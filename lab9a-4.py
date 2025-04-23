lst = ['madam', 'Python', 'malayalam', 12321]

for item in lst:
    if str(item) == str(item)[::-1]:
        print(f"Palindrome: {item}")