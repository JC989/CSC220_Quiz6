import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Create a max heap despite the fact that Python only has a min heap feature,
        #this is necessary because we need to efficiently access the heaviest stones
        #which is accomplished by inverting the weights and using a max heap
        #Create a max heap by inverting the stone weights
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        #Continue until there is one or no stones left
        while len(max_heap) > 1:
            #Pop the two heaviest stones
            stones1 = -heapq.heappop(max_heap)
            stones2 = -heapq.heappop(max_heap)
            #If they are not equal, push the difference back into the heap
            if stones1 != stones2:
                #Push the difference back into the heap, this is done to simulate the smashing of stones
                heapq.heappush(max_heap, -(stones1-stones2))
        #Return the weight of the last stone or 0 if no stones are left
        return -max_heap[0] if max_heap else 0
    


        