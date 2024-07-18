class Solution:
    def countBits(self, n: int) -> List[int]:
        ans  = list()

        for i in range(0,n+1):
            binary = bin(i).replace("0b", "")
            binary_str = str(binary)
            b_sum = sum(int(digit) for digit in binary_str)

            ans.append(b_sum)

        return ans


        