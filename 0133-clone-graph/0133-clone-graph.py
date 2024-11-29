"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # 시간복잡도: 노드 개수n, 간선을 m이라고 했을 때 O(n + m)
    # 공간복잡도: 노드 개수에 대해 O(n)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        dequeue = deque([node])
        clones = {node.val: Node(node.val, [])}
        while dequeue:
            current = dequeue.popleft()
            current_clone = clones[current.val]

            for neighbor in current.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    dequeue.append(neighbor)

                current_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]