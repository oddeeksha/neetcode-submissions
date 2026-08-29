import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
            else:
                heapq.heappush(stones, x)
                break
            if y > x :
                heapq.heappush(stones, x-y)
        if stones:
            return -1 * heapq.heappop(stones)
        else:
            return 0 

