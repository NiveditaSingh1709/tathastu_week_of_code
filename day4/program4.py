n=int(input("enter the number of elements"))
my_dict = dict()
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
result = {}

for key,value in my_dict.items():
    if value not in result.values():
        result[key] = value

print(result)
#for remove duplicate values:
