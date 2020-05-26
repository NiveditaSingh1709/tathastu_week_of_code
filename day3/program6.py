def sum(List,size,sum):
    sumList=[]
    if size==1:
        for i in List:
            sumList.append(sum+i)
        return sumList
    L1=list(List)
    for i in List:
        L1.remove(i)
        sumList.extend(sum(L1,size-1,sum+i))
    return sumList
def summation(List,size):
    sumList=list(List)
    for i in range(2,size+1):
        sumList.extend(sum(List,i,0))
    number=1
    while True:
        if number not in sumList:
            print("the least interger which is not present in the list:",number)
            break
        number+=1
size=int(input("enter the number of elements in the list"))
List=[]
print("enter the elements")
for i in range(size):
    List.append(int(input()))
summation(List,size)
