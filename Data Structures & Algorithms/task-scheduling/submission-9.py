class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        q = deque()

        count = Counter(tasks)
        maxHeap = [(-cnt,task) for task,cnt in count.items()]
        heapq.heapify(maxHeap)
        print(maxHeap)
        order = []
        while maxHeap or q:
            time += 1

            while q and q[0][1] == time:
                count, idle, task = q.popleft()
                heapq.heappush(maxHeap, (count,task))

            if maxHeap:
                curr, task = heapq.heappop(maxHeap)
                order.append(task)
                cnt = 1 + curr
                if cnt:
                    q.append((cnt, n + time + 1, task))
            else:
                order.append("-")
            
        #print(order)
        return time




