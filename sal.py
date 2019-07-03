a=input()
m=0
for i in range(len(a)):
 if(a[i].isdigit() or a[i].isalpha() or a[i]==(" ")):
  continue
 else:
  m+=1
print(m)
