pali=input("enter a word: ")
n=len(pali)
palin=True
for i in range(n//2):
    if pali[i]!=pali[n-1-i]:
        palin=False
if palin:
    print(pali,"is an palindrome")
else:
    print(pali,"is not an palindrome")

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")