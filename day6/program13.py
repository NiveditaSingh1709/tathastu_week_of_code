def countTriplets(arr, n, a, b):
    ans = 0
    for i in range (0, n - 2):
        for j in range (i + 1, n - 1):
            for k in range (j + 1, n):
                if ((arr[i] + arr[j] + arr[k] >= a)
                        and (arr[i] + arr[j] + arr[k] <= b)):
                    ans += 1
    return ans
if __name__ == "__main__":
    arr = [2, 7, 5, 3, 8, 4, 1, 9]
    n = len (arr)
    a = 8;
    b = 16
    print (countTriplets (arr, n, a, b))
