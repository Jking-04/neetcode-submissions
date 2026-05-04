class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        current_streak = 1
        max_streak = 0

        for num in num_set:
            if (num -1) not in num_set:
                current=num
                current_streak = 1

                while current+1 in num_set:
                    current+=1
                    current_streak+=1

            max_streak = max(current_streak, max_streak)

        return max_streak


        