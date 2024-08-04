class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, loc: List[int]) -> int:
        # start1, start2 -> loc1, loc2 -> startAngle -> endAngle, scan
        # [angle vs loc] -> bisect
        arr = []
        base = 0
        for p in points:
            dx, dy = (p[0] - loc[0]), (p[1] - loc[1])
            if dx == 0 and dy == 0:
                base += 1
                continue
            arr.append(math.degrees(math.atan2(dx, dy)))
        arr.sort()
        length = len(arr)
        for i in range(length):
            arr.append(arr[i] + 360)
        ret = base
        for i in range(length):
            idx = bisect.bisect_right(arr, arr[i] + angle)
            ret = max(ret, idx - i + base)
        return ret
        
