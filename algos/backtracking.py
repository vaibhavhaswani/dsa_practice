### Power Set Problem
## 📌 Given a set of numbers, generate all possible subsets.

def subsets(numbers):
    sets=[] #subset tracker
    
    def backtrack(idx,track):
        sets.append(track[:])                  #append all the sets in track
        for i in range(idx,len(numbers)):        # from given index to all the numbers
            track.append(numbers[i])            # update tracker with number at index
            backtrack(i+1,track)           #recursively track another index with updated tracker
            track.pop()                  # pop to elemeneaet or backtrack
    
    backtrack(0,[]) #instantiate with first number element and empty tracker
    
    return sets

## Testcase
# Input: [1, 2, 3]  
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

# Test
print(subsets([1, 2, 3]))

#📌 Problem: Given an array of distinct numbers, return all possible permutations (different orderings).

def permute(nums):
    perms=[]
    
    def backtrack(start):
        if start==len(nums):
            perms.append(nums[:])
            return 
        for i in range(start,len(nums)):
            nums[start],nums[i]=nums[i],nums[start]
            backtrack(start+1)
            nums[start],nums[i]=nums[i],nums[start]
    
    backtrack(0)
    return perms

## test case for permute
perms=permute([1,2,3])
print(perms)     