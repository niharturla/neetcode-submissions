class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # use bfs to find height of tree

        # to traverse through every combination, it will take O(n)

        # construct adjList

        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        heights = []
        for i in range(n):
            visited = set()

            stack = []
            stack.append((i,0))
            h = 0
            while stack:
                node, depth = stack.pop()
                visited.add(node)
                for nei in adjList[node]:
                    if nei not in visited:
                        stack.append((nei, depth + 1))
                h = max(h,depth)
            heights.append((i,h))

        heights = [height[1] for height in heights]
        # take all heights that are minimum 
        min_h = min(heights)
        res = []
        for node in range(n):
            if heights[node] == min_h:
                res.append(node)
        return res


