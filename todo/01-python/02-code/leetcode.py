from typing import List
from collections import Counter


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        :param nums: [2,7,11,15]
        :param target: 9
        :return: [0,1]
        """
        ret_lst = []
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    ret_lst.append(i)
                    ret_lst.append(j)
                    break

        return ret_lst

    def two_sum_2(self, nums: List[int], target: int) -> List[int]:
        ret_lst = []
        for i in range(len(nums)):
            num = nums[i]
            num2 = target - num
            if num2 in nums[i + 1:]:
                j = nums[i + 1:].index(num2) + 1 + i
                ret_lst = [i, j]
                break

        return ret_lst

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order,
        remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same.
        :param nums: [0,0,1,1,1,2,2,3,3,4]
        :return: 5 (nums = [0,1,2,3,4,_,_,_,_,_])
        """
        counter = Counter(nums)
        # 从后往前删除重复元素
        for i, (_, v) in enumerate(reversed(counter.items())):
            # len-i:保留后不重复的元素，+1:保留重复元素的第一个
            head = len(nums) - i - v + 1
            tail = len(nums) - i
            del nums[head: tail]

        return len(nums)

    def remove_duplicates_2(self, nums: List[int]) -> int:
        """
        !remove是有问题的
        """
        uni_lst = []
        loops = len(nums)
        i = 0
        while loops > 0:
            val = nums[i]
            if val not in uni_lst:
                uni_lst.append(val)
                i = i + 1
            else:
                nums.remove(val)
            loops = loops - 1

        return len(nums)

    def remove_duplicates_3(self, nums: List[int]) -> int:
        uni_lst = []
        loops = len(nums)
        i = 0
        while loops > 0:
            val = nums[i]
            if val not in uni_lst:
                uni_lst.append(val)
                i = i + 1
            else:
                nums.pop(i)
            loops = loops - 1

        return len(nums)

    def remove_element(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val,
        remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
        :param nums: [3,2,2,3]
        :param val: 3
        :return: 2(nums = [2,2,_,_])
        """
        idx = 0
        counts = len(nums)
        while idx < counts:
            item = nums[idx]
            if item == val:
                nums.remove(item)
                counts = counts - 1
            else:
                idx = idx + 1

        return len(nums)

    def remove_element_2(self, nums: List[int], val: int) -> int:


sol = Solution()
lst = [3, 2, 2, 3]
lst = [0, 1, 2, 2, 3, 0, 4, 2]
lst = []
val = 2
re = sol.remove_element(lst, val)
print(re)
print(lst)
