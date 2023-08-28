class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1:
            return nums
        
        p = 1
        a = p-1
        b = p

        while p <= l-1:
            while a >= 0 and nums[b] < nums[a]:
                # swap elements at position a and b
                nums[a],nums[b] = nums[b],nums[a]

                # look at the pair one to the left of the current pair
                a -= 1
                b -= 1
            p += 1
            a = p-1
            b = p
        return nums
