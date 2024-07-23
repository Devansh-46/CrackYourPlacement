def is_possible(stalls, k, mid):
    # Can we place k cows with at least mid distance between them?
    cows_count = 1
    last_pos = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= mid:
            cows_count += 1
            if cows_count == k:
                return True
            last_pos = stalls[i]
    return False

def solve(n, k, stalls):
    stalls.sort()
    s = 0
    e = stalls[-1] - stalls[0]

    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if is_possible(stalls, k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        k = int(data[index])
        index += 1
        stalls = list(map(int, data[index:index+n]))
        index += n
        
        ans = solve(n, k, stalls)
        results.append(ans)
    
    for result in results:
        print(result)
