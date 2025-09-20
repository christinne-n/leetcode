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
                
"""
Plus One (Easy)
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
class Solution: #O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1): #loops through the digits array backwards, starting from last element, ending at -1 and decrementing by 1
            digits[i] += 1 #increments the current digit by 1
            if digits[i] < 10: #checks if the current digit is less than 10
                return digits   #if <10 returns the digits array
            else:
                digits[i] = 0  #if >=10 sets the current digit to 0 and continues the loop to increment the next digit
        digits.insert(0, 1) #if all digits were 9, carry over to a new digit, so insert 1 at index 0
        return digits #returns the digits array
