n=int(input("enter the number of elements"))
my_dict = dict()
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(list(sorted(my_dict.values()))[-2])
#find the second maximum in dictionary
