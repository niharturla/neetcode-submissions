class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap


        # O(m * n), where n is tasks and m is idle time
        time = 0
        q = deque()

        count = Counter(tasks)
        print(count)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, n + time))
            while q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time




