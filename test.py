
#1 Duplicate Integer:
class Solution:
    
    ex: nums: [1,2,3,3]
    create empty set    
    check for loop for duplicate and check set
    if x in set then return true else false
    
    def hasDuplicate(self, nums: List[int]) -> bool:
         seen = set()
         for x in nums:
            if x in seen:
                return True
            seen.add(x)
            return False

#2 Valid Anagram
class Solution:
        ex: s = racecar, t = carrace
        check length if not the same return false.
        for loop s then check the frequency of all letters.
def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s))
            countS[s[i]] = 1 + countS.get(s[i], 0)
            print(countS)


#3 Two Integer Sum

ex: Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

enumerate to get the index and values
create dictionary
prev = {}
for i, val in enumerate(num)
    diff = target - val
    if diff in prev:
       return [prev[r], i]
    prev = i


#4 anagram groups:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #mapping character count of from list of anagrams 
        for s in strs:
            count = [0] * 26 #lowercase a-z
            for c in s:
                count[ord(c) - ord("a")]  += 1
                
            res[tuple(count)].append(s)

        return res.values()

#5 Products of Array Discluding Self

    Input: nums = [1,2,4,6]

    Output: [48,24,12,8]

    if is 1 return product of everything else
    ex: 1 product = 48 (2 x 4 x 6)

    go from last to beginning 

    class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) #(length of nums)
        prefix = 1 #(index for prefix )
        
        for i in range(len(nums))
            res[i] = prefix #(updates index)
            prefix *= nums[I] #(prefix multiple nums[I] )
        postfix = 1
        for i in range(len(nums) -1, -1, -1): #(up to beginning)
            res[i] *= postfix
            postfix *= nums[i]
        return res


#6 Valid Palindrome

  checkv is initialized to an empty string and checks if its alpha numeric
and append each word to lowercase 
returning true or false with checkv word and inverse of checkv

  checkv = ""
        for each in s:
            if each.isalnum():
                checkv += each.lower()
        return checkv == checkv[::-1]


#7 Two Sum pointer
L is initialized at the end of the list. 
r is initialized at the beginning of the list.
We compare summation (numbers[l] + numbers[r]) to the target and decrease l  or increase r.
ex: Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

 l, r=0, len(numbers) - 1
    
        while l < r: 
            if numbers[l] + numbers[r] == target: return (l + 1, r + 1)
            if numbers[l] + numbers[r] > target: r-=1
            else: l+=2


#8 3sum
class Solution:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

enumerate both nums have 2 pointers for left and right of nums;
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums)
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, lens(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l+= 1
            return res

#9 Water Container
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by an array [1,8,6,2,5,4,8,3,7]. In this case, the maximum area of water (blue section) the container can contain is 49.

I am using 2 pointers and comparing them to see if they are at least the same height as the calc—the max area.


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r
            area = (r - l) * min (height[l], height[r])
            max_area = max (max_area, area)
            
            if height[l] < height[r]
                l += 1
            else:
                r -= 1

        return res


#10 Trapping Rain Water

 heights =  [0,2,0,3,1,0,1,3,2,1]
 output = 9

have two-pointers at the beginning and end of the list. set two variables at the current element 
then increase the left or decrease  the right pointer if it's less or greater. subtract from previous element to the current one on left or right in a if else statement that calc. the result.


        l, r = 0, len(heights) - 1
        leftMax = heights[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
            leftMax = max(leftMax,height[l])
            res += leftMax -height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

#11 Best time to buy and sell stocks
Input: prices = [10,1,5,6,7,1]
price for each price,  the lowest is the previous price unless it is lower than the price. 
max difference in price and lowest.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res 

#12 Longest Substring Without Duplicates
Input: s = "zxyzxyz"

Output: 3

check for each letter in the string add them to the set, and then count each removal if the letter is found in the set
    x = set()
        l = 0
        for each in s:
            if each in x:
                x.remove(each)
                l +=1
            x.add(each)
        return l



#13 class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
       
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l +1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l +1)
        return res


#14 class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

#15 class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "()", "]":"[", "}":"{"} 

         Mapping the closing brackets with the opening ones
        and using the stack for which ones are matched.
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop
        return not stack
