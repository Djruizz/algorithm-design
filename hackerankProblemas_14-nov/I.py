s = input()
def isPalindrome(string):
    return string == string[::-1]

counter = 0
for i in range(len(s)):
    for j in range(i, len(s)+1):
        if s[i:j] != "" and isPalindrome(s[i:j]):
            counter+= 1
print(counter)