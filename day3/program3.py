def removeDuplicate(str):
    s=set(str)
    s = "".join (s)
    print ("after the string:", s)
    t = ""
    for i in str:
        if (i in t):
            pass
str=input("enter the string")
removeDuplicate (str)
