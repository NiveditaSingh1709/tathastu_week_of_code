from itertools import permutations
number=input("enter the number")
choices=list(map(int,number))
res=permutations(number)  
res2=[]
for i in res:
    res2.append(int(''.join(i)))
res2=sorted(res2)
print(res2[res2.index(int(number))+1]) 
