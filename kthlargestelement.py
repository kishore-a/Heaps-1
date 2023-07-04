from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in range(len(nums)):
            heapq.heapify(q)
            heapq.heappush(q, nums[i])
            if (len(q) > k):
                heapq.heappop(q)
        return heapq.heappop(q)
