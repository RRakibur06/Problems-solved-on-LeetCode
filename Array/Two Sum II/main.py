class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        firstPointer = 0
        lastPointer = len(numbers) - 1
        
        while True:
            x = numbers[firstPointer] + numbers[lastPointer]
            
            if x == target:
                break  
            elif x < target:
                firstPointer += 1
            else:
                lastPointer -= 1
        
        return [firstPointer + 1, lastPointer + 1]

        