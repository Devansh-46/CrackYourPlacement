def isPossible(a, b, n, k):
    
    a.sort(reverse=True)

    b.sort()

    for i in range(n):
        if (a[i] + b[i] < k):
            return False

    return True


# Driver code

a = [2, 1, 3]
b = [7, 8, 9]
k = 10
n = len(a)

if(isPossible(a, b, n, k)):
    print("Yes")
else:
    print("No")