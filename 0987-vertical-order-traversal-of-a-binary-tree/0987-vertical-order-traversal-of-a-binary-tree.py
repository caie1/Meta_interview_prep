from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = float('inf')
        max_column = float('-inf')

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])  # (node, row, column)

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    if node.left:
                        queue.append((node.left, row + 1, column - 1))
                    if node.right:
                        queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret
