class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            second = target - i
            if not second in nums[nums.index(i)+1:]: #if the first number is equal to second --> [3,4,2] with 6 as target but there are no further matching elements
                continue #jumps to the next loop
            if second == i and second in nums[::-1]: # if
                return [nums.index(i),( len(nums)-nums[::-1].index(second) )-1]
            elif second in nums:
                return [nums.index(i),nums.index(second)]


class Sol1:
    def twoSum(self,list,target):
        for i in list:
            second = target - i
            if not second in list[list.index(i)+1:]:
                continue
            if second == i and second in list[list.index(i),len(list)- list[::-1].index(second) - 1]:
                return [list.index(i),(len(list)-list[::-1].index(second)) -1]
            elif second in list:
                return[list.index(i),list.index(second)]

