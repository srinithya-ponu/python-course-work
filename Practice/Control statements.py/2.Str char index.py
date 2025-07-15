s= 'Jash Nithya Aashritha Sai Shobith Hari'.lower()
n=len(s)
ch=input("Enter the char:").lower()

for i in range(n):
    if s[i]==ch:
        print(ch,i)



#Enter the char:a
#a 1
#a 10
#a 12
#a 13
#a 20
#a 23
#a 35