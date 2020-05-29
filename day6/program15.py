def FindElement(A, n):
    for i in range (0, n, 1):
        flag = 0
        for j in range (0, i, 1):
            if (A[j] >= A[i]):
                flag = 1
                break
        for j in range (i + 1, n, 1):
            if (A[j] <= A[i]):
                flag = 1
                break
        if (flag == 0):
            return A[i]
    return -1
if __name__ == '__main__':
    A = [4, 3, 2, 5, 8, 6, 7]
    n = len (A)
    print (FindElement (A, n))
