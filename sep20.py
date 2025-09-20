"""
Two Sum (Easy)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution: #O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)): #loops through each element in nums
            for j in range(i+1, len(nums)): #loops through each element after i
                if nums[i]+nums[j] == target: #checks if the sum of the two elements is equal to target
                    return [i,j] #returns the indices of the two elements
                