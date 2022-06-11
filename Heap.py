"""
Function to return the minimum cost of connecting the ropes.
"""
def minCost(self,arr,n) :
    # python has min heap
    import heapq
    heapq.heapify(arr)
    res = 0
    while(len(arr) > 1):
        elem1 = heapq.heappop(arr)
        elem2 = heapq.heappop(arr)
        res += (elem1 + elem2)
        heapq.heappush(arr, elem1 + elem2)
    return res