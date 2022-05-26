def maxcross(arr,l,mid,h):
    sm=0
    left=-100000

    for i in range(mid,l-1,-1):
        sm+=arr[i]
        if sm>left:
            left=sm
    sm=0
    right=-100000

    for i in range(mid+1,h+1):
        sm+=arr[i]
        if sm>right:
            right=sm
    return max(left+right, left, right)
    
def maxarray(arr, l, h):
    if l==h:
        return arr[l]
    mid = (l+h)//2
    return max(maxarray(arr,l,mid),maxarray(arr,mid+1,h),maxcross(arr,l,mid,h))

class Solution:
       
    
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sums = maxarray(nums, 0, n-1)
        return sums
    
    
