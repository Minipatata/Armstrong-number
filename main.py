num=int(input("Please enter any desired number of your choice"))
guessed=num
num=str(num)
l=len(num)
sum=0

for i in num:
    s=int(i)**3
    sum=sum+s
if sum==guessed:
    print("This number is an armstrong number")
else:
    print("This number is not an armstrong number")