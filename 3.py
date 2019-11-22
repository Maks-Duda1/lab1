s=str(input("Enter your text:"))
a=s[: :-1]
b=a.split()
c=" ".join(reversed(b))
print(c)