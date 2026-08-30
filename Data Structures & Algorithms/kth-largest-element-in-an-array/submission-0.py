import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        maxx = 0
        for i in range(k):
            maxx = heapq.heappop(nums)
        return -maxx


        