class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        ns = sorted(nums)

        for i in range(len(ns)):
            if i> 0 and ns[i] == ns[i-1]:
                continue
            
            left = i+1
            right =len(ns) - 1

            while left < right:
                total = ns[i] + ns[left] + ns[right]

                if total >0:
                    right -= 1
                elif total <0:
                    left += 1
                else:
                    results.append([ns[i], ns[left], ns[right]])
                    left += 1
                    while left < right and ns[left] ==ns[left-1]:
                        left += 1

        return results


