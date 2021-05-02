a=input("請輸入A的好友:").split(" ")
b=input("請輸入B的好友:").split(" ")
ans =0
for i in range(0,len(a)):
    if a[i] in b:
        ans+=1
print(ans)
