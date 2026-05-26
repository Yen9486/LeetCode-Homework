class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True
            
        root = [i for i in range(n)]
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                root[root_y] = root_x
                
        for u, v in edges:
            union(u, v)
            
        return find(source) == find(destination)